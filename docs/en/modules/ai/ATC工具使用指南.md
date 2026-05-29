---
title: Tools
---

# Tools

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ATC工具使用指南/ATC工具使用指南.md
--- # Preface
**Overview** This document describes how to convert network models from open-source frameworks (such as Caffe, Onnx, etc.) into offline models supported by the image analysis engine using ATC (Advanced Tensor Compiler). During the model conversion process, operator scheduling optimization, weight data rearrangement, and memory usage optimization can be achieved. The preprocessing of the model can be completed without a device. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Target Audience** This document is primarily intended for the following engineers: - Technical support engineers
- Software development engineers The following experience and skills are helpful for understanding this document: - Familiarity with basic Linux commands.
- Basic understanding of machine learning and image analysis methods. **Symbol Conventions** The following symbols may appear in this document, with their meanings described below. **Change History**

| Document Version | Date | Description |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First release. |

# Introduction

<a name="ZH-CN_TOPIC_0000002441981281"></a>## Tool Functional Architecture The functional architecture of the ATC tool is shown in [Figure 1](#fig16910569311). As shown in [Figure 1](#fig16910569311), users can convert open-source framework network models into offline models suitable for the image analysis engine using the ATC tool. They can also convert the converted offline model into a json file for easy viewing. Users can also directly convert open-source framework network model files into json files through the ATC tool. **Figure 1** ATC Tool Functional Architecture ## Tool Running Flow The overall flow of model conversion using the ATC tool is shown in [Figure 1](#fig125822392014). **Figure 1** Running Flow The detailed flow is described as follows: - Before using the ATC tool, install ATC in the development environment and locate the ATC tool in the relevant path. For details, see the environment preparation in [Getting the ATC Tool](#ZH-CN_TOPIC_0000002441981281).[¶](#tool-functional-architecture-the-functional-architecture-of-the-atc-tool-is-shown-in-figure-1-as-shown-in-figure-1-users-can-convert-open-source-framework-network-models-into-offline-models-suitable-for-the-image-analysis-engine-using-the-atc-tool-they-can-also-convert-the-converted-offline-model-into-a-json-file-for-easy-viewing-users-can-also-directly-convert-open-source-framework-network-model-files-into-json-files-through-the-atc-tool-figure-1-atc-tool-functional-architecture-tool-running-flow-the-overall-flow-of-model-conversion-using-the-atc-tool-is-shown-in-figure-1-figure-1-running-flow-the-detailed-flow-is-described-as-follows-before-using-the-atc-tool-install-atc-in-the-development-environment-and-locate-the-atc-tool-in-the-relevant-path-for-details-see-the-environment-preparation-in-getting-the-atc-tool "锚链接")

<a name="ZH-CN_TOPIC_0000002442021333"></a>- Prepare the model to be converted and upload it to the development environment. For details, see [Conversion Example](#ZH-CN_TOPIC_0000002442021333).
<a name="ZH-CN_TOPIC_0000002441981037"></a>- Use the ATC tool for model conversion. When configuring related parameters, choose whether to perform [Quantization Options](#ZH-CN_TOPIC_0000002441981037) based on the actual situation. Image preprocessing is a hardware image preprocessing module provided by the image analysis engine, including color gamut conversion and image normalization (mean subtraction/coefficient multiplication). # Getting Started

## Preparations ### Getting the ATC Tool Install the CANN package independently. For details, see "2.3.4 Software Package Installation" in the Driver and Development Environment Installation Guide. This manual takes the independent installation of the CANN package for ATC as an example. ### Setting Environment Variables > **Note:** > - Environment variables set using the export method are only valid in the current window. If users have previously set ATC installation path environment variables in the .bashrc file, they need to manually delete the originally set ATC installation path environment variables before executing the above commands.[¶](#preparations-getting-the-atc-tool-install-the-cann-package-independently-for-details-see-234-software-package-installation-in-the-driver-and-development-environment-installation-guide-this-manual-takes-the-independent-installation-of-the-cann-package-for-atc-as-an-example-setting-environment-variables-note-environment-variables-set-using-the-export-method-are-only-valid-in-the-current-window-if-users-have-previously-set-atc-installation-path-environment-variables-in-the-bashrc-file-they-need-to-manually-delete-the-originally-set-atc-installation-path-environment-variables-before-executing-the-above-commands "锚链接")

> - If users have previously set ATC installation path environment variables for a previous version in the .bashrc file, they need to manually delete the originally set ATC installation path environment variables before executing the atc command, then set the following environment variables. After setting, switch to a new window to execute the atc model conversion command. **Mandatory Environment Variables** (In the following environment variables, ${install\_path} uses the default installation path of the software package as an example) `export PATH=${install_path}/Ascend/ascend-toolkit/{software version}/atc/bin:$PATH export LD_LIBRARY_PATH=${install_path}/Ascend/ascend-toolkit/{software version}/atc/third_party_lib:$LD_LIBRARY_PATH` Or execute the following command to configure environment variables: `source ${install_path}/Ascend/ascend-toolkit/{software version}/x86_64-linux/script/setenv.sh` ### Conversion Example This section provides an example of model conversion using the ATC tool, including the basic command format and usage. ### Output File Description After model conversion, the ATC tool outputs the following files: - Offline model file (\*.om): The converted offline model file.
> - JSON file (\*.json): A description file for the model structure (optional, generated when the --output\_type=JSON parameter is specified). # Parameter Description

## Overview This section describes the parameters supported by the ATC tool. The ATC tool parameters are categorized into basic functions, quantization options, and image preprocessing configurations. ## Basic Functions The basic function parameters of the ATC tool include model input/output specification, framework type selection, operator configuration, and precision mode settings. **Model Conversion Parameters** [¶](#overview-this-section-describes-the-parameters-supported-by-the-atc-tool-the-atc-tool-parameters-are-categorized-into-basic-functions-quantization-options-and-image-preprocessing-configurations-basic-functions-the-basic-function-parameters-of-the-atc-tool-include-model-inputoutput-specification-framework-type-selection-operator-configuration-and-precision-mode-settings-model-conversion-parameters "锚链接")

| Parameter | Description | Mandatory/Optional |
| --- | --- | --- |
| --model | Specifies the input model file path. | Mandatory |
| --framework | Specifies the framework type of the input model. | Mandatory |
| --output | Specifies the output model file path and name. | Mandatory |
| --soc\_version | Specifies the chip version. | Mandatory |

### Image Preprocessing Configuration Image preprocessing is configured starting with the `--aapp_op` parameter, which identifies the AAPP (Advanced Application Pre-Processing) operator configuration. All input configurations are described within the aapp\_op. - `related_input_rank` parameter (optional): Identifies which input of the model to apply image preprocessing to, starting from 0. Default is 0. For example, if the model has two inputs and preprocessing needs to be applied to the second input, configure related\_input\_rank as 1. - Type: Integer - Range: >= 0 - Input image format when running on the device side (mandatory): - Type: enum - Range: YUV420SP, YVU420SP, YUV422SP, YVU422SP, YUV400, BGR\_PLANAR, RGB\_PLANAR, RGB\_PACKAGE, BGR\_PACKAGE, XRGB\_PLANAR, ARGB\_PLANAR, XBGR\_PLANAR, ABGR\_PLANAR, RGBX\_PLANAR, RGBA\_PLANAR, BGRX\_PLANAR, BGRA\_PLANAR, XRGB\_PACKAGE, ARGB\_PACKAGE, XBGR\_PACKAGE, ABGR\_PACKAGE, RGBX\_PACKAGE, RGBA\_PACKAGE, BGRX\_PACKAGE, BGRA\_PACKAGE, RAW\_RGGB, RAW\_GRBG, RAW\_GBRG, RAW\_BGGR - Original model training image format (channel data order, optional): - Type: enum ### Quantization Options The ATC tool provides quantization options to convert float32 models into lower-precision (such as int8 or float16) models for improved inference performance.

