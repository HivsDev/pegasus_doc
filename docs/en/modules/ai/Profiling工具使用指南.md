---
title: Profiling
---

# Profiling

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Profiling工具使用指南/Profiling工具使用指南.md
--- # Preface
**Overview** This document provides a detailed description of the constraints, environment preparation, and specific operation guidance for the Profiling tool, as well as common FA Qs and troubleshooting methods. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Intended Audience** This document is mainly applicable to developers. **Symbol Conventions** The following symbols may appear in this document, and their meanings are as described below.

| Symbol | Description |
| --- | --- |
| | Indicates a high-risk hazard which, if not avoided, will result in death or serious injury. |

**Revision History**

| **Document Version** | **Release Date** | **Revision Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Overview

## Feature Introduction The Profiling performance analysis tool is used to collect and analyze key performance metrics at various runtime stages of inference tasks (applications or operators) running on the SoC. Users can optimize key performance bottlenecks based on the output performance data to achieve ultimate product performance. The Profiling performance analysis tool collects, analyzes, and summarizes hardware and software performance data during the execution of an application project. - Hardware performance data includes: PMU metrics of modules such as *AA* Core, *AA* Vector Core, and system hardware performance indicators.[¶](#feature-introduction-the-profiling-performance-analysis-tool-is-used-to-collect-and-analyze-key-performance-metrics-at-various-runtime-stages-of-inference-tasks-applications-or-operators-running-on-the-soc-users-can-optimize-key-performance-bottlenecks-based-on-the-output-performance-data-to-achieve-ultimate-product-performance-the-profiling-performance-analysis-tool-collects-analyzes-and-summarizes-hardware-and-software-performance-data-during-the-execution-of-an-application-project-hardware-performance-data-includes-pmu-metrics-of-modules-such-as-aa-core-aa-vector-core-and-system-hardware-performance-indicators "锚链接")

- Software performance data includes: performance metrics of modules such as ACL. ## Solution Introduction Current inference tasks mainly support the following scenarios for collecting and parsing Profiling data of inference tasks, as shown in [Figure 1](#fig47010185593). Board-side collection, development environment parsing. **Figure 1** Separate Collection and Parsing Method
 In this scenario, the application project must first be developed in the development environment (such as Ubuntu 18.04). During development, the application project can enable Profiling by adding a configuration file acl.json or calling the ACL API interface. When the application is executed on the board side, Profiling data collection is enabled. After collection is complete, the output data is copied to the **development environment** for data parsing. ## Scenario Introduction Currently, when Profiling is performed on the Ascend AA processor used for inference, Profiling data is obtained and parsed mainly through the CANN software package, as shown in [Table 1](#table159711027195516). **Table 1** CANN Software Package Profiling Enablement Description

| Software Package | Profiling Enablement Description |
| --- | --- |
| Development Toolkit Ascend-cann-toolkit | **Collect** Profiling data of the application project during inference by configuring acl.json or through the ACL API interface. |
| Debugging Toolkit, containing the Profiling data parsing tool msprof.pyc. Its Profiling functions are as follows. msprof.pyc: **Collects and parses** Profiling data of the application project via a Python script tool. |

Application scenario description: The Ascend device has the development toolkit Ascend-cann-toolkit installed, which serves as both the development environment and the runtime environment for running applications. In this scenario, Profiling data can be collected on the board side via acl.json or ACL API, and then copied to the environment where the CANN package is located for parsing using the Profiling parsing tool msprof.pyc. Users can perform all Profiling operations in this scenario. When users need to engage in development activities such as coding, compiling, running, and debugging, this scenario is recommended. # Usage Constraints
Using the Profiling function has the following constraints: - Before using the Profiling function, ensure the umask value of the executing user is greater than or equal to 0027; otherwise, the directories and file permissions of the obtained Profiling data may be too permissive. - To view the umask value, execute the command: **umask** - To modify the umask value, execute the command: **umask *new\_value*** - Profiling provides two methods: acl.json and ACL API. The priority order is: command-line acl.json > ACL API. If using the ACL API method, ensure the Profiling switch in the acl.json file is set to off.
- Profiling does not support initiating multiple Profiling runs based on the same result directory, as this may lead to inaccurate collected data. For example, if the main program contains multiple independent inference tasks, this issue may occur when calling Profiling.
- It is not supported to start multiple Profiling tasks simultaneously on the same Device side.
- When configuring Profiling-related paths, only paths consisting of letters, numbers, and underscores are supported. Paths with special characters are not supported.
- The Profiling function and the Dump function cannot be used simultaneously. Before starting Profiling, close data Dump. Reason: If both are enabled simultaneously, Dump operations will affect system performance, causing inaccurate Profiling performance metrics.
- If the disk space of the configured dump path is full during Profiling data collection, performance data may fail to be written to disk. Therefore, users must ensure sufficient disk space. Additionally, the raw performance data written to disk must be aged by the user to prevent disk space from being fully occupied.
- If the disk or user directory space of the configured dump path is full during Profiling data parsing, parsing may fail or files may not be written. Users must clean up the disk or user directory space themselves.
- The Profiling tool requires Python 3.7.5. It is recommended to use Python 3.7.5.
- Application project development must follow the "Application Development Guide" manual, calling the **svp\_acl\_init()** interface to complete ACL initialization and the **svp\_acl\_finalize()** interface to complete ACL de-initialization, in order to obtain complete Profiling performance data. > **Note:**

> If the application has called the **svp\_acl\_init()** interface but not the **svp\_acl\_finalize()** interface, resulting in an abnormal end of the Profiling flow, the collected data will be incomplete. Data already collected by Profiling within the last 1 second may be lost due to untimely synchronization, but the lost data will not exceed 2M, and it will not affect the analysis of already synchronized performance data. # Profiling Flow
> The overall inference Profiling flow is shown in [Figure 1](#fig1160371182910). Follow the flow to prepare the environment in advance, develop applications or operators, collect Profiling performance data, and parse Profiling performance data. **Figure 1** Profiling Flow
> **Table 1** Profiling Flow Description

| Step | Description |
| --- | --- |
| Environment Preparation | Before enabling Profiling, set up the environment for Profiling data collection and parsing. See [Environment Preparation](#ZH-CN_TOPIC_0000002408421302) for details. |
| Collect Profiling Data | Before collecting Profiling data, refer to the "Application Development Guide" for application development. Copy the application executable to the runtime environment, run it, and collect Profiling data. For collection via acl.json, see [Collecting Profiling Data via acl.json](#ZH-CN_TOPIC_0000002408581342); for collection via ACL API, see [Collecting Profiling Data via ACL API](#ZH-CN_TOPIC_0000002442020433). |
| Parse Profiling Data | Parse Profiling data and export corresponding data using the script tool msprof.pyc. See [Parsing Profiling Data](#ZH-CN_TOPIC_0000002408581254) for details. |

# Environment Preparation
Before using the Profiling function, set up the relevant environment based on the [Scenario Introduction](#ZH-CN_TOPIC_0000002441980705). Details are as follows. See Section "2.1 Board-Side Environment Installation" in the "Driver and Development Environment Installation Guide" to set up the board-side and development environment. For scenarios with separate development and runtime environments: See Section "2.3 Command-Line Development Environment Installation" in the "Driver and Development Environment Installation Guide" to install dependencies, toolchains, and the CANN package. # Quick Start

## msprof.pyc Script Tool Introduction The msprof.pyc script tool is a Profiling command-line tool written in Python. Its functionality and installation path are as follows. Function: Collect and parse Profiling performance raw data. Path: ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof > **Note:**[¶](#msprofpyc-script-tool-introduction-the-msprofpyc-script-tool-is-a-profiling-command-line-tool-written-in-python-its-functionality-and-installation-path-are-as-follows-function-collect-and-parse-profiling-performance-raw-data-path-install_dirtoolkittoolsprofilerprofiler_toolanalysismsprof-note "锚链接")

> - This section uses the Profiling tool installation directory "${INSTALL\_DIR}" as an example.
> - Replace ${INSTALL\_DIR} with the file storage path after CANN software installation, e.g., $HOME/Ascend/ascend-toolkit/svp\_latest/x86\_64-linux.
> - The Profiling tool is run using the ordinary user created during installation (e.g., HwHi\_Aa\_User). Therefore, unless otherwise specified, all operations in this document are performed by this user.
> - If the original parsing file model is only loaded or unloaded without executing the relevant execute inference interface, the Profiling tool will not generate related data by default. ## One-Click Profiling This function runs the application executable, calls the acl.json file, reads Profiling-related configurations, and automatically collects performance raw data. After successful raw data collection, the collected data can be copied to the development environment with the CANN software package for performance data parsing, generating relevant csv and json files of parsed data. 1. Follow the steps below to configure the acl.json file and complete application compilation and running: - When calling ATC model conversion, configure the following parameter to set the current model as a debug-type model supporting Profiling. `--online_model_type=2` - Open the project file, check the called **svp\_acl\_init()** function, and obtain the acl.json file path. See [2](#ZH-CN_TOPIC_0000002408581342#li66486291273) for details. - Modify the acl.json file specified by the svp\_acl\_init method, add Profiling-related configurations in the following format. For specific parameter configuration, see [3](#ZH-CN_TOPIC_0000002408581342#li1333417325516). `{ "profiler":{ "output":"/root/Ascend Projects/My App Test/profiling", "aacpu":"on", "aac_metrics":"ArithmeticUtilization", "interval":"0", "acl_api":"on", "switch":"on" } }` > **Note:** >- For detailed methods of compiling and running application projects, refer to the "Application Development Guide". >- When using this method, be sure to call the **svp\_acl\_init()** interface to complete ACL initialization and **svp\_acl\_finalize()** to complete ACL de-initialization. >- The acl.json does not need to be configured; a default acl.json configuration will be generated during Profiling collection. 2. To establish an SSH connection, the user needs to provide a corresponding configuration file with a .ini extension. Configure the file in the xxx.ini format as follows. See [Table 1](#table1631953814614) for parameter descriptions. `[ssh_config] ip = XXXX username = XXXX pwd = XXX port = XX` **Table 1** ini Configuration File Parameters 
> | Parameter | Description |
> | --- | --- |
> | ip | IP address for logging into the board |
> | username | Username for logging into the board |
> | pwd | Password of the board user |
> | port | Port number for SSH connection, default is 22 |
> > **Note:** >- Users should delete the configuration file after use or encrypt it to prevent leakage of the board-side username and password. >- The collection process automatically mounts the Profiling directory to the server address. To prevent insufficient board-side space preventing data collection, ensure sufficient space in the server mount path. 3. Execute the following command to perform board-side operations: `python3.7.5 msprof.pyc collect -m <main> --config <config> --all` After executing the board-side collection command, SSH will upload the corresponding project to the board and execute the main executable. The JOB data generated on the board will be transferred back to the corresponding local output path. For a detailed introduction to the msprof.pyc tool, see [msprof.pyc Script Tool Introduction](#ZH-CN_TOPIC_0000002408581270). For a detailed description of command-line parameters, see [Collecting Profiling Data](#ZH-CN_TOPIC_0000002408421366). 4. The JOB data is generated and parsed in the corresponding output directory, generating summary and timeline directories, as shown in [Figure 1](#fig1489718583120). **Figure 1** Parsed Results in summary and timeline Directories # Collecting Profiling Data

## Collecting Profiling Data via acl.json Run the application executable, call the acl.json file, and read Profiling-related configurations to automatically collect performance raw data. After successful raw data collection, copy the collected raw data to the development environment with the CANN software package for performance data parsing and display of parsing results. > **Note:**[¶](#collecting-profiling-data-via-acljson-run-the-application-executable-call-the-acljson-file-and-read-profiling-related-configurations-to-automatically-collect-performance-raw-data-after-successful-raw-data-collection-copy-the-collected-raw-data-to-the-development-environment-with-the-cann-software-package-for-performance-data-parsing-and-display-of-parsing-results-note "锚链接")

> For detailed methods of compiling and running application projects, refer to the "Application Development Guide".
> When using this method, be sure to call the **svp\_acl\_init()** interface to complete ACL initialization and **svp\_acl\_finalize()** to complete ACL de-initialization. **Collect Performance Raw Data** Follow the steps below to configure the acl.json file and complete application compilation and running. 1. When calling ATC model conversion, configure the following parameter to set the current model as a debug-type model supporting Profiling. `--online_model_type=2` 2. Open the project file, check the called **svp\_acl\_init()** function, and obtain the acl.json file path. For example, as shown in [Figure 1](#fig374885405310). **Figure 1** acl.json File Path > **Note:** >If svp\_acl\_init() is initialized as empty, modify the function to add the path of the acl.json created in [2](#li66486291273). 3. Modify the acl.json file specified by the svp\_acl\_init method, add Profiling-related configurations in the following format. `{ "profiler":{ "output":"/root/Ascend Projects/My App Test/profiling", "aacpu":"on", "aac_metrics":"ArithmeticUtilization", "interval":"0", "acl_api":"on", "switch":"on" } }` profiler parameter configuration description: - switch: Profiling switch, values on or off. Optional parameter. on means Profiling is enabled, off means Profiling is disabled; if this parameter is missing or its value is not on, Profiling is disabled. - output: Output path for Profiling performance data on the local running server. Optional parameter. After Profiling collection ends, a JOB-starting directory is generated under this path, storing the raw Profiling performance data. Each directory corresponds to data from one Device. Supports absolute or relative paths (relative to the current path when executing the command): - Absolute path starts with "/", e.g., /home/HwHi\_Aa\_User/mdc/output. It is recommended to use the project path/profiling as the output path. - If the directory set here does not exist, the collected result data is stored in the directory where the application executable is located by default (ensure the runtime user configured during installation has read/write permissions for that directory). > **Note:** >The directory specified by this parameter must be created in advance, and the runtime user configured during installation must have read/write permissions. - *aa* cpu: Switch for collecting *aa* cpu data, optional on or off, default is on. Optional parameter. - **aac**\_metrics: *AA* Core collection events. Currently only supports Arithmetic Utilization. Configuring it as Arithmetic Utilization indicates collecting *pattern recognition* Core performance data; otherwise, no collection. - acl\_api: Switch for collecting acl api data, optional on or off, default is on. Optional parameter. - interval: Sampling interval based on inference intervals, default is 0. For example, performing inference on 1000 images with batch\_num set to 100 and looping 10 times; setting Inference Interval to 2 means collecting performance data every 200 images. - After configuring acl.json, recompile and run the application project according to the "Application Development Guide". 4. The Profiling performance raw data is generated under the path specified by output, as shown in [Figure 2](#fig296631712496). > **Note:** >- When interval is not configured as 0, for fast inference execution, the disk write speed may not keep up with inference completion speed, possibly resulting in fewer reports than expected. In such cases, it is recommended to add sleep during each inference round to ensure sufficient disk write time. >- The collected Profiling performance raw data may fill the disk. Ensure sufficient disk space is reserved. 5. Use the command-line tool to synchronize the compiled project to the board side via SSH for collection. > **Note:** >When using SSH, install the paramiko component first. You can install it using pip3.7.5 install paramiko. During collection, a profiling folder is created in the board-side directory. It is recommended to mount the profiling directory locally. An example command is as follows, where profiling refers to the directory on the board-side environment (create it first if it does not exist). `mount -t nfs -o nolock,tcp NFS_Server_IP:Server_Absolute_Path user_home/profiling` > **Note:** >Mounting the profiling directory to the server address prevents insufficient board-side space from preventing data collection. Ensure sufficient server mount path space. Execute the following command for board-side operations. See [Table 1](#table26771257162016) for parameter descriptions. `python3.7.5 msprof.pyc collect -m <main> --config <config> [--all]` After executing the board-side collection command, SSH will upload the corresponding project to the board and execute the main executable. The JOB data generated on the board will be transferred back to the corresponding local target path. **Table 1** Data Collection Command Parameters
> | Parameter | Description | Optional/Required |
> | --- | --- | --- |
> | -m, --main | Executable file main in the project to run on the board | Required |
> | --config | Path to the SSH configuration file; see Table 1 for usage | Required |
> | --interval | Set interval num in acl.json, default 0 | Optional |
> | --acl\_api | Set whether to enable acl\_api in acl.json, default is on | Optional |
> | --aacpu | Set whether to enable aacpu in acl.json, default is on | Optional |
> | --switch | Set whether to enable switch in acl.json, default is on | Optional |
> | --aac\_metrics | Set aac\_metrics in acl.json, default is Arithmetic Utilization | Optional |
> | --output | Set the output path for generated jobs | Optional |
> | --all | Parse the JOB file after board-side execution | Optional (one-click collection and parsing requires adding the all command) |
> **Figure 2** Profiling Performance JOB Raw Data ## Collecting Profiling Data via ACL API See Section "8.6 Profiling Performance Data Collection" in the "Application Development Guide". # Parsing Profiling Data

## Parsing Profiling Data Before parsing Profiling data in any directory, refer to [Collecting Profiling Data](#ZH-CN_TOPIC_0000002408421366) to collect the corresponding data. 1. Log in to the **development environment** as the runtime user of the Toolkit component package Ascend-cann-toolkit. Use the HwHi\_Aa\_User user as an example.[¶](#parsing-profiling-data-before-parsing-profiling-data-in-any-directory-refer-to-collecting-profiling-data-to-collect-the-corresponding-data-1-log-in-to-the-development-environment-as-the-runtime-user-of-the-toolkit-component-package-ascend-cann-toolkit-use-the-hwhi_aa_user-user-as-an-example "锚链接")

1. Switch to the directory where the msprof.pyc script is located, such as ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof. > **Note:** >Tip: For convenience, the HwHi\_Aa\_User user can execute the command **alias msprof='python3.7.5 ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof/msprof.pyc'** to set an alias. Afterward, there is no need to enter the ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof directory; simply enter **msprof** from any directory to execute the Profiling command. >Replace ${INSTALL\_DIR} with the file storage path after CANN software installation, e.g., $HOME/Ascend/ascend-toolkit/svp\_latest/x86\_64-linux. 3. Execute the following command to parse Profiling data in any directory. The following parsing methods are supported, as described below. Parse Profiling data in any directory. See [Table 1](#zh-cn_topic_0300758037_table23221111184312) for parameter descriptions. `python3.7.5 msprof.pyc import [-h] -dir <dir>` For example: **python3.7.5 msprof.pyc import -dir** \_/home/HwHi\_Aa\_User/JOBXXXX > **Note:** >When using the import method to parse Profiling data, even if the .db file already exists in the original Profiling data directory, this method will regenerate the .db file. **Table 1** Parse Any Directory Command Parameters 

 | Parameter | Description | Optional/Required |
 | --- | --- | --- |
 | -h, --help | Display help information, only for obtaining usage instructions. | Optional |
 | -dir, --collection-dir | Collected Profiling data directory. Must specify a JOBXXX directory containing a data folder and the corresponding info.json.0 file. | Required |

 4. After executing the above command, a sqlite directory will be generated under the corresponding JOBXXX directory, and a .db file will be generated under the sqlite directory. ## Timeline Data Description ### Exporting Timeline Data Before exporting timeline data, refer to [Parsing Profiling Data](#ZH-CN_TOPIC_0000002408581254). Follow the steps below to export timeline data. 1. Log in to the **development environment** as the runtime user of the Toolkit component package Ascend-cann-toolkit. Use the HwHi\_Aa\_User user as an example.
2. Switch to the directory where the msprof.pyc script is located, such as ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof. > **Note:** >Tip: For convenience, the HwHi\_Aa\_User user can execute the command **alias msprof='python3.7.5 ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof/msprof.pyc'** to set an alias. Afterward, there is no need to enter the ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof directory; simply enter **msprof** from any directory to execute the Profiling command. >Replace ${INSTALL\_DIR} with the file storage path after CANN software installation, e.g., $HOME/Ascend/ascend-toolkit/svp\_latest/x86\_64-linux. 3. Execute the following command to export timeline data. The command-line format is as follows. See [Table 1](#zh-cn_topic_0290106133_table23221111184312) for parameter descriptions. `python3.7.5 msprof.pyc export timeline [-h] -dir <dir>` For example, the command to export inference or system Profiling timeline data is as follows: **python3.7.5 msprof.pyc export timeline -dir** */home/HwHi\_Aa\_User/JOBXXX* **Table 1** Export Timeline Data Command Parameters 

 | Parameter | Description | Optional/Required |
 | --- | --- | --- |
 | -h, --help | Display help information, only for obtaining usage instructions. | Optional |
 | -dir, --collection-dir | Collected Profiling data directory. Must specify a JOB\_XXX directory containing a data folder and the corresponding info.json.0 file. | Required |

 4. After executing the above command, a timeline directory is generated under the collection-dir directory. Different data generates corresponding json files. See [Table 2](#zh-cn_topic_0290106133_table972265435020) for details. **Table 2** Timeline File Description 

 | Data Category | Timeline File Name | Description |
 | --- | --- | --- |
 | Task Timeline Parsed Data | task\_time\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json | Task Scheduler task scheduling information. See [Task Scheduler Task Scheduling Information Data Description](#ZH-CN_TOPIC_0000002408421346) for details. |
 | ACL Timeline Parsed Data | acl\_{device\_id}.{model\_file\_name}.{model\_id}.{batch\_num}.json | ACL interface timing data. To generate this file, the collected Profiling data must contain files starting with AclModule. See [ACL Interface Timing Data Description](#ZH-CN_TOPIC_0000002441980605) for details. |

 [Table 3](#table64582512342) shows a comparison of the timeline data files contained after collection, parsing, and export via acl.json or ACL API. **Table 3** Generated Data File Comparison 

 | File Name Included | acl.json | ACL API |
 | --- | --- | --- |
 | task\_time\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json | Included | Included |
 | acl\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json | Included | Included |

 > **Note:** >- Files in the timeline directory are generated based on the actual Profiling data collected. If the actual Profiling data does not contain relevant data files, the corresponding timeline data will not be exported. >- The export command can directly export data files from parsed Profiling data. When Profiling data has not been parsed, executing the export command alone can also parse Profiling data and export data files. >- The generated json (chrome trace) file can be opened and viewed in a Chrome browser by entering "chrome:/tracing" in the address bar and dragging the saved file into the blank area. The file descriptions below all use this method. For the chrome trace format, refer to the [chrome trace introduction](https:/docs.google.com/document/d/1CvA Clv FfyA5R-PhY Umn5OO Qt YMH4h6I0n Ss KchN Ay SU/edit). >- Time nodes (not Timestamps) involved in the exported data are system monotonic time, related only to the system, not real time. ### Task Scheduler Task Scheduling Information Data Description See [Exporting Timeline Data](#ZH-CN_TOPIC_0000002442020445) to obtain the Task Scheduler task scheduling information data file. task\_time\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json, where {device\_id} is the device ID, {model\_file\_name} is the model name, {model\_id} is the model ID, and {batch\_num} is the number of batches. task\_time\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json displayed in Chrome browser is shown in [Figure 1](#fig117501624516). **Figure 1** Chrome Browser Display
 Key field descriptions are shown in [Table 1](#zh-cn_topic_0300758050_table446285293613). **Table 1** Field Descriptions

| Field | Description |
| --- | --- |
| name | Layer name, concatenated if fused layers |
| pid | Process Id abbreviation |
| tid | Thread Id abbreviation |
| dur | Duration Time abbreviation, used to calculate the end time |
| args->Task Type | Execution unit, such as \_AA\_ CORE, \_AA\_ CPU |
| args->Stream Id | Stream ID, default 0 |
| args->Task Id | Execution order index value, starting from 0 |

### ACL Interface Timing Data Description See [Exporting Timeline Data](#ZH-CN_TOPIC_0000002442020445) to obtain the ACL interface timing data file acl\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json, where {device\_id} is the device ID, {model\_file\_name} is the model name, {model\_id} is the model ID, and {batch\_num} is the number of batches. acl\_{deviceid}.{model\_file\_name}.{model\_id}.{batch\_num}.json displayed in Chrome browser is shown in [Figure 1](#fig16128291478). **Figure 1** Chrome Browser Display
Key field descriptions are shown in [Table 1](#zh-cn_topic_0300758050_table446285293613). **Table 1** Field Descriptions

| Field | Description |
| --- | --- |
| Title | Interface name of the selected component. For example, in this example, it is the aclmdl Query Size interface of Thread 132397. |
| Start | Time point on the timeline axis in the display; chrome trace auto-aligns. |
| Wall Duration | Duration of the current interface call, in ms. |
| Mode | API type. |
| Process\_Id | Process ID where the ACL API is located. |
| Thread\_Id | Thread ID where the ACL API is located. |

## Summary Data Description ### Exporting Summary Data Before exporting summary data, refer to [Parsing Profiling Data](#ZH-CN_TOPIC_0000002408581254) to parse the Profiling data. Follow the steps below to export summary data. 1. Log in to the **development environment** as the runtime user of the Toolkit component package Ascend-cann-toolkit. Use the HwHi\_Aa\_User user as an example.
2. Switch to the directory where the msprof.pyc script is located, such as ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof. > **Note:** >Tip: For convenience, the HwHi\_Aa\_User user can execute the command alias msprof='python3.7.5 ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof/msprof.pyc' to set an alias. Afterward, there is no need to enter the ${INSTALL\_DIR}/toolkit/tools/profiler/profiler\_tool/analysis/msprof directory; simply enter msprof from any directory to execute the Profiling command. >Replace ${INSTALL\_DIR} with the file storage path after CANN software installation, e.g., $HOME/Ascend/ascend-toolkit/svp\_latest/x86\_64-linux. 3. Execute the following command to export summary data. The command-line format is as follows. See [Table 1](#zh-cn_topic_0290119915_table23221111184312) for parameter descriptions. `python3.7.5 msprof.pyc export summary [-h] -dir <dir> [--format <export_format>]` For example, the command to export inference or system Profiling summary data is as follows: **python3.7.5 msprof.pyc export summary -dir** */home/HwHiAaUser/JOBXXX* **--format** *csv* **Table 1** Export Summary Data Command Parameters

| Parameter | Description | Optional/Required |
| --- | --- | --- |
| -h, --help | Display help information, only for obtaining usage instructions. | Optional |
| -dir, --collection-dir | Collected Profiling data directory. Must specify a JOB\_XXX directory containing a data folder and the corresponding info.json.0 file. | Required |
| --format | Export format for summary data files. Supports csv and json, default is csv. | Optional |

> **Note:** >The summary file descriptions below use the csv file as an example. 4. After executing the above command, a summary directory is generated under the collection-dir directory. Different data (inference, system) generates corresponding csv files. See [Table 2](#zh-cn_topic_0290119915_table2434544115813) for details. **Table 2** Summary File Description 

| Data Category | Summary File Name | Description |
| --- | --- | --- |
| *AA* Core Metrics | op\_summary\_{device\_id}.{model\_file\_name}.{model\_id}.{batch\_num}.{input\_pic\_num}.{current\_pic\_count}.{icache\_miss\_rate}.{frequency}.csv | Instruction proportion data for each Core. To generate this csv file, the collected Profiling data must contain files starting with *AA\_core. This file serves as the input file for interface display.* |
| Statistics-ACL API | acl\_statistic*{model\_id}*}.csv | Statistics of all ACL API call durations and comparison of average, maximum, and minimum durations for the same API. |
| Statistics-Ops | op\_statistic\_{device\_id*{model\_id}**{iter\_id}.csv* | Statistics of all layer run durations and comparison of average, maximum, and minimum durations for the same layer. |

[Table 3](#table64582512342) shows a comparison of the summary data files contained after collection, parsing, and export via acl.json and ACL API. **Table 3** Generated Data File Comparison 

| File Name Included | acl.json | ACL API |
| --- | --- | --- |
| op\_summary}.{model\_file\_name}.{model\_id}.{batch\_num}.{input\_pic\_num}.{current\_pic\_count}.{icache\_miss\_rate}.{frequency}.csv | Included | Included |
| acl\_statistic\_{device\_id*{model\_id}*}.csv | Included | Included |
| op\_statistic\_{device\_id*{model\_id}*.csv | Included | Included |

>}\_{iter\_id **Note:** >- Files in the summary directory are generated based on the actual Profiling data collected. If the actual Profiling data does not contain relevant data files, the corresponding summary data will not be exported. >- The export command can directly export data files from parsed Profiling data. When Profiling data has not been parsed, executing the export command alone can also parse Profiling data and export data files. >- Tip: When opening the generated summary data file with Excel, field values may appear in scientific notation, e.g., "1.00159E+12". In this case, select the cell, right-click > Format Cells, select "Number" under the "Number" tab, and click "OK" to display normally. >- When certain field values in the generated summary data file show "N/A", it means the value does not exist at that time. >- Time nodes (not Timestamps) involved in the exported data are system monotonic time, related only to the system, not real time. ### ACL Interface Call Count and Timing Data Description See [Exporting Summary Data](#ZH-CN_TOPIC_0000002408421430) to obtain the ACL interface call count and timing data file acl\_statistic\_{device\_id}\_{model\_id}\_{iter\_id}.csv, where {device\_id} is the device ID, {model\_id} is the model ID, and {iter\_id} is the iteration ID. The content format example of acl\_statistic\_{device\_id}\_{model\_id}\_{iter\_id}.csv is shown in [Figure 1](#fig11375113204916). **Figure 1** CSV File Content
The column descriptions of the exported ACL interface timing data table are as follows. **Table 1** Field Descriptions 

| Parameter | Parameter Description |
| --- | --- |
| Process ID | Process ID where the corresponding API is called. |
| Thread ID | Thread ID where the corresponding API is called. |
| Type | Type of the called ACL API, such as model, runtime. |
| Name | Name of the called API. |
| Total Time Ratio(%) | Proportion of total time for the called API. |
| Total Time(us) | Duration of the called API, in us. Click the triangle next to the field to sort in descending or ascending order by this value. |
| Count | Number of times the corresponding API is called. |
| Avg(us) | Average duration per single call of the corresponding API, in us. |
| Max(us) | Maximum duration per single call of the corresponding API, in us. |
| Min(us) | Minimum duration per single call of the corresponding API, in us. |

### *AA* Core Data Description See [Exporting Summary Data](#ZH-CN_TOPIC_0000002408421430) to obtain the *AA* Core data file op\_summary\_{device\_id}.{model\_file\_name}.{model\_id}.{batch\_num}.{input\_pic\_num}.{current\_pic\_count}.{icache\_miss\_rate}.{frequency}.csv, where {device\_id} is the device ID, {model\_file\_name} is the model name, {model\_id} is the model ID, {batch\_num} is the batch number, {input\_pic\_num} is the total number of input images, {current\_pic\_count} is the current image count, {icache\_miss\_rate} is the icache miss rate, {frequency} is the frequency, and {iter\_id} is the iteration ID. The content format example of the full-network scenario op\_summary csv file is shown in [Table 1](#table1942315910414). **Table 1** Field Descriptions

| Field | Field Description |
| --- | --- |
| Layer Id | Layer ID |
| Ori Layer Name | Original layer name |
| Layer Name | Layer name |
| Layer Type | Layer type |
| Time(us) | Current layer duration |
| Time Ratio | Percentage of current layer duration in total duration |
| Mac Busy Ratio | Percentage of cube-type instructions (matrix operation instructions) in the current layer total duration. |
| Mac Ppen Ratio | Percentage of effective working time for cube-type instructions (matrix operation instructions) in the current layer total duration. |
| Vec Busy Ratio | Percentage of vector-type instructions (vector operation instructions) in the current layer total duration. |
| Vec Ppen Ratio | Percentage of effective working time for vector-type instructions (vector operation instructions) in the current layer total duration. |
| Dstr Ratio | Full name: data store ratio. Percentage of memory transfer time (writing internal data to external DDR) in the current layer total duration. |
| Dtrans Ratio | Full name: internal data transfer and transform ratio. Percentage of data movement time (mainly RAM-to-RAM transfer with various transforms) in the current layer total duration. |
| DLD Ratio | Full name: data\_loading\_ratio. Percentage of image and featuremap loading time in the current layer total duration. |
| WLD Ratio | Full name: weight\_loading\_ratio. Percentage of weight loading time in the current layer total duration. |
| Memory Bound | Used to identify whether there is a Memory bottleneck during \_AA\_ Core operator execution. Calculated by max(Dstr Ratio, DLD Ratio, WLD Ratio)/max(Mac Busy Ratio, Vec Ppen Ratio). A result less than 1 indicates no Memory bottleneck; greater than 1 indicates a Memory bottleneck, with larger values indicating more severe bottlenecks. |
| DDR Read(byte) | DDR read bytes |
| DDR Write(byte) | DDR write bytes |
| DDR Total(byte) | Sum of DDR read and write bandwidth |

> **Note:**
> - If the Input Shapes value of the operator is empty, displayed in the format "; ; ; ;", it indicates that the current input is a scalar, where ";" is the delimiter for each dimension. The same applies for operator output dimensions.
> - In the performance data, "-" represents the total layer data information. ### *AA* Core Operator Call Count and Timing Data Description See [Exporting Summary Data](#ZH-CN_TOPIC_0000002408421430) to obtain the *AA* Core operator call count and timing data file op\_statistic\_{device\_id}\_{model\_id}\_{current\_pic\_count}\_{iter\_id}.csv, where {device\_id} is the device ID, {model\_id} is the model ID, {current\_pic\_count} is the current image count, and {iter\_id} is the iteration ID. The content format example of the full-network scenario op\_statistic csv file is shown in [Table 1](#table1942315910414). **Table 1** Field Descriptions

| Field | Field Description |
| --- | --- |
| Task ID | Auto-incrementing Task ID |
| Stream ID | Stream ID where the corresponding OP is called. |
| OP Name | Operator name of the OP. |
| Task Type | Describes whether it is \_AA\_ CORE or \_AA\_ CPU |
| Total Time Ratio(%) | Proportion of total time for the called OP. |
| Total Time(us) | Duration of the called OP, in us. Click the triangle next to the field to sort in descending or ascending order by this value. |
| Count | Number of times the corresponding OP is called. |