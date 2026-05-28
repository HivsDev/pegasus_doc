---
title: OTP
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/OTP API 参考/OTP API 参考.md
--- # Preface
**Overview** OTP is a non-volatile memory. Its main characteristic is that once the bit content of the corresponding storage space is written from 0 to 1, or after locking the corresponding area according to the lock mechanism, it can no longer be modified. OTP is mainly used to store specific data, such as the root key for the CIPHER module, security enable flags, and other information. > **Note:**

> Unless otherwise specified, the content for and , and , and Hi3403V100 is identical. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document, and their meanings are described below.

| Symbol | Description |
| --- | --- |
| | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History** The revision history summarizes the changes made in each document update. The latest version of the document includes updates from all previous document versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Overview
The OTP module provides MPI interfaces for driving one-time programmable operations, enabling CIPHER module root key Flashing, jtag key Flashing, key Flashing status verification, and user reserved space data read/write. ## Key Usage Mechanism in OTP **Figure 1** Key Usage Mechanism in , OTP
**Figure 2** Key Usage Mechanism in Hi3403V100, OTP
## OTP Usage Notes When OTP is deployed in different scenarios, its usage may vary. - In the Linux environment - User-mode OTP can be used by linking the static library libss\_otp.a or the dynamic library libss\_otp.so, depending on libsecurec.a or libsecurec.so. - Kernel-mode OTP uses module insertion, i.e., insmod ot\_otp.ko, which depends on ot\_osal.ko, ot\_base.ko, sys\_config.ko, and ot\_sys.ko. - In the OPTEE environment, the user-mode OTP external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_tee\_xxx.
- In the UBOOT environment, the user-mode OTP external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_mpi\_xxx. # API Reference
OTP provides the following AP Is: - [ss\_mpi\_otp\_init](#ZH-CN_TOPIC_0000002457868853): Initializes the OTP module.
- [ss\_mpi\_otp\_deinit](#ZH-CN_TOPIC_0000002457828757): Deinitializes the OTP module.
- [ss\_mpi\_otp\_set\_user\_data](#ZH-CN_TOPIC_0000002457828753): Sets OTP user space data.
- [ss\_mpi\_otp\_get\_user\_data](#ZH-CN_TOPIC_0000002424349934): Reads OTP user space data.
- [ss\_mpi\_otp\_set\_user\_data\_lock](#ZH-CN_TOPIC_0000002424349926): Sets OTP user data lock.
- [ss\_mpi\_otp\_get\_user\_data\_lock](#ZH-CN_TOPIC_0000002457868865): Gets OTP user data lock.
- [ss\_mpi\_otp\_burn\_product\_pv](#ZH-CN_TOPIC_0000002424190098): Burns PV data and lock flags to the chip internal OTP.
- [ss\_mpi\_otp\_read\_product\_pv](#ZH-CN_TOPIC_0000002424349922): Reads PV data or lock flags from the chip internal OTP.
- [ss\_mpi\_otp\_get\_key\_verify\_status](#ZH-CN_TOPIC_0000002457828745): Gets the verification status of the KEY stored in the chip internal OTP. ## ss\_mpi\_otp\_init [Description] Initializes the OTP module. [Syntax] `td_s32 ss_mpi_otp_init(td_void);` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] Initialization and deinitialization must be paired. [Example] None. ## ss\_mpi\_otp\_deinit [Description] Deinitializes the OTP module. [Syntax] `td_s32 ss_mpi_otp_deinit(td_void);` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] Initialization and deinitialization must be paired. [Example] None. ## ss\_mpi\_otp\_set\_user\_data [Description] Sets OTP user space data. [Syntax] `td_s32 ss_mpi_otp_set_user_data(const td_char *field_name, td_u32 offset, const td_u8 *value, td_u32 value_len);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| field\_name | Field name. | Input |
| offset | OTP user space address offset. | Input |
| value | User space data to set. | Input |
| value\_len | Length of the user space data to set (unit: byte). | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The parameter field\_name is set with reference to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- offset must be 4-byte aligned.
- value\_len is the byte length of value.
- The valid ranges for offset and value\_len refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide". offset + value\_len must not exceed the maximum byte length. [Example] None. ## ss\_mpi\_otp\_get\_user\_data [Description] Gets OTP user space data. [Syntax] `td_s32 ss_mpi_otp_get_user_data(const td_char *field_name, td_u32 offset, td_u8 *value, td_u32 value_len);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| field\_name | Field name. | Input |
| offset | OTP user space address offset. | Input |
| value | User space data retrieved. | Output |
| value\_len | Length of the user space data to retrieve (unit: byte). | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The parameter field\_name is set with reference to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- offset must be 4-byte aligned.
- value\_len is the byte length of value.
- The valid ranges for offset and value\_len refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide". offset + value\_len must not exceed the maximum value. [Example] None. ## ss\_mpi\_otp\_set\_user\_data\_lock [Description] Sets OTP user space data lock. [Syntax] `td_s32 ss_mpi_otp_set_user_data_lock(const td_char *field_name, td_u32 offset, td_u32 value_len);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| field\_name | Field name. | Input |
| offset | OTP user space address offset. | Input |
| value\_len | Length of the user space data lock (unit: byte). | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The parameter field\_name is set with reference to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- offset must be 4-byte aligned.
- The valid ranges for offset and value\_len refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide". offset + value\_len must not exceed the maximum value. [Example] None. ## ss\_mpi\_otp\_get\_user\_data\_lock [Description] Gets OTP user space data lock. [Syntax] `td_s32 ss_mpi_otp_get_user_data_lock(const td_char *field_name, td_u32 offset, td_u32 value_len, ot_otp_lock_status *lock);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| field\_name | Field name. | Input |
| offset | OTP user space address offset. | Input |
| value\_len | Length of the user space data lock to retrieve (unit: byte). | Input |
| lock | Lock status retrieved. | Output |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The parameter field\_name is set with reference to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- offset must be 4-byte aligned.
- The valid ranges for offset and value\_len refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide". offset + value\_len must not exceed the maximum value. [Example] None. ## ss\_mpi\_otp\_burn\_product\_pv [Description] Burns PV data and lock flags to the chip internal OTP. [Syntax] `td_s32 ss_mpi_otp_burn_product_pv(const ot_otp_burn_pv_item *pv, td_u32 num);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| pv | PV data group to burn. | Input |
| num | Number of PV data groups to burn. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The burn member of parameter pv must be set to TD\_TRUE.
- The field\_name member of parameter pv is set with reference to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The value\_len member of parameter pv is the bit length of value, refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The value member of parameter pv is set with reference to the "Description" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The lock member of parameter pv takes the value TD\_TRUE or TD\_FALSE. For field\_name entries with auto-lock in the "Description" column of Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide", any configuration will result in locking.
- The valid range for parameter num is 1 to 500. [Example] None. ## ss\_mpi\_otp\_read\_product\_pv [Description] Reads PV data or lock flags from the chip internal OTP. [Syntax] `td_s32 ss_mpi_otp_read_product_pv(ot_otp_burn_pv_item *pv, td_u32 num);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| pv | PV data group retrieved. | Input and Output |
| num | Number of PV data groups to retrieve. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] - The burn member of parameter pv must be set to TD\_FALSE.
- The field\_name member of parameter pv refers to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The value\_len member of parameter pv is the bit length of value, refer to the "Bit Width" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The value member of parameter pv refers to the "Description" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide".
- The valid range for parameter num is 1 to 500. [Example] None. ## ss\_mpi\_otp\_get\_key\_verify\_status [Description] Gets the verification status of the KEY stored in the chip internal OTP. [Syntax] `td_s32 ss_mpi_otp_get_key_verify_status(const td_char *key_name, td_bool *status);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| key\_name | KEY field name to verify. | Input |
| status | KEY verification status retrieved. | Output |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349930). |

[Requirements] - Header files: ot\_common\_otp.h, ss\_mpi\_otp.h
- Library file: libss\_otp.a [Notes] The parameter key\_name refers to the "Field Name" column in Section 2.2 "S Sxxxx OTP Field Definitions" of the "Security Subsystem Usage Guide". [Example] None. # Data Types
The relevant data types and data structures are defined as follows: - [ot\_otp\_burn\_pv\_item](#ZH-CN_TOPIC_0000002457868869): OTP PV data type.
- [ot\_otp\_lock\_status](#ZH-CN_TOPIC_0000002424190110): Defines OTP data lock status.
- [OT\_OTP\_PV\_NAME\_MAX\_LEN](#ZH-CN_TOPIC_0000002457828749): Maximum byte length of field name (unit: byte).
- [OT\_OTP\_PV\_VALUE\_MAX\_LEN](#ZH-CN_TOPIC_0000002424349938): Maximum byte length of the value member in ot\_otp\_burn\_pv\_item (unit: byte). ## ot\_otp\_burn\_pv\_item [Description] OTP PV data type. [Definition] `typedef struct { td_bool burn; td_char field_name[OT_OTP_PV_NAME_MAX_LEN]; td_u32 value_len; td_u8 value[OT_OTP_PV_VALUE_MAX_LEN]; td_bool lock;
} ot_otp_burn_pv_item;` [Members]

| Member Name | Description |
| --- | --- |
| burn | Whether to burn. TD\_TRUE for Flashing, TD\_FALSE for reading. |
| field\_name | Field name. |
| value\_len | Data bit width length (unit: bit). |
| value | Data buffer. |
| lock | Whether to lock. |

[Notes] value\_len indicates the bit width length of value. [Related Data Types and Interfaces] - [ss\_mpi\_otp\_burn\_product\_pv](#ZH-CN_TOPIC_0000002424190098)
- [ss\_mpi\_otp\_read\_product\_pv](#ZH-CN_TOPIC_0000002424349922) ## ot\_otp\_lock\_status [Description] Defines OTP data lock status. [Definition] `typedef enum { OT_OTP_STA_ALL_UNLOCKED = 0, /**< user data area is all unlock. */ OT_OTP_STA_PARTIAL_LOCKED, /**< user data area is partial unlock. */ OT_OTP_STA_ALL_LOCKED, /**< user data area is all lock. */ OT_OTP_STA_BUTT, /**< invalid param. */
} ot_otp_lock_status;` [Members]

| Member Name | Description |
| --- | --- |
| OT\_OTP\_STA\_ALL\_UNLOCKED | The currently retrieved user space is all unlocked. |
| OT\_OTP\_STA\_PARTIAL\_LOCKED | The currently retrieved user space is partially locked. |
| OT\_OTP\_STA\_ALL\_LOCKED | The currently retrieved user space is all locked. |
| OT\_OTP\_STA\_BUTT | Data buffer. |

[Notes] None. [Related Data Types and Interfaces] [ss\_mpi\_otp\_get\_user\_data\_lock](#ZH-CN_TOPIC_0000002457868865) ## OT\_OTP\_PV\_NAME\_MAX\_LEN [Description] Maximum byte length of field name (unit: byte). [Definition] ```

# define OT\_OTP\_PV\_NAME\_MAX\_LEN 32[¶](#define-ot_otp_pv_name_max_len-32 "锚链接")

`[Members] None. [Notes] None. [Related Data Types and Interfaces] - [ss\_mpi\_otp\_burn\_product\_pv](#ZH-CN_TOPIC_0000002424190098)
- [ss\_mpi\_otp\_read\_product\_pv](#ZH-CN_TOPIC_0000002424349922) ## OT\_OTP\_PV\_VALUE\_MAX\_LEN<a name="ZH-CN_TOPIC_0000002424349938"></a> [Description] Maximum byte length of the value member in ot\_otp\_burn\_pv\_item (unit: byte). [Definition]`

# define OT\_OTP\_PV\_VALUE\_MAX\_LEN 32[¶](#define-ot_otp_pv_value_max_len-32 "锚链接")

``` [Members] None. [Notes] None. [Related Data Types and Interfaces] - [ss\_mpi\_otp\_burn\_product\_pv](#ZH-CN_TOPIC_0000002424190098)
- [ss\_mpi\_otp\_read\_product\_pv](#ZH-CN_TOPIC_0000002424349922) # Error Codes
The error codes provided by OTP are as follows. **Table 1** OTP module error codes

| Error Code | Macro Definition | Description |
| --- | --- | --- |
| 0x804e0001 | OT\_ERR\_OTP\_NOT\_INIT | Device not initialized |
| 0x804e0002 | OT\_ERR\_OTP\_NULL\_PTR | Null pointer in parameters |
| 0x804e0003 | OT\_ERR\_OTP\_BUSY | Device busy |
| 0x804e0004 | OT\_ERR\_OTP\_FAILED\_INIT | Initialization failed |
| 0x804e0005 | OT\_ERR\_OTP\_FAILED\_MEM | Memory allocation failed |
| 0x804e0006 | OT\_ERR\_OTP\_FAILED\_SEC\_FUNC | Security function call failed |
| 0x804e0007 | OT\_ERR\_OTP\_INVALID\_PARAM | Invalid parameter |
| 0x804e0008 | OT\_ERR\_OTP\_INVALID\_FIELD\_NAME | Field name does not match |
| 0x804e0009 | OT\_ERR\_OTP\_ZONE\_ALREADY\_SET | User space already set |
| 0x804e000a | OT\_ERR\_OTP\_ZONE\_LOCKED | User space already locked |
| 0x804e000b | OT\_ERR\_OTP\_ZONE\_NO\_PERMIT | No user space permission |
| 0x804e000c | OT\_ERR\_OTP\_WAIT\_TIMEOUT | Wait timeout |
| 0x804e000d | OT\_ERR\_OTP\_FUNC\_UNSUPPORT | Function not supported |

# Acronyms and Abbreviations

| | | |
| --- | --- | --- |
| **A** | | |
| AES | Advanced Encryption Standard | Advanced Encryption Standard |
| **K** | | |
| KLAD | Key Ladder | Key Ladder |
| **O** | | |
| OTP | One Time Programmable | One Time Programmable |
| **S** | | |
| SPACC | Security Protocol Accelerator | Security Protocol Accelerator |