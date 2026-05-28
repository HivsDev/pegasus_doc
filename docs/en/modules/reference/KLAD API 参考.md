---
title: KLAD
---

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/KLAD API 参考/KLAD API 参考.md
--- # Preface
**Overview** KLAD is the key management module, integrating key derivation, plaintext KEY transfer, and ROOTKEY hierarchical transfer. > **Note:**

> Unless otherwise specified in this document, the content for and Hi3403V100 is completely identical. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document, and their meanings are described below.

| Symbol | Description |
| --- | --- |
| | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History**

| Document Version | Release Date | Change Description |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Overview

## Overview KLAD is the key management module. It supports key derivation, plaintext KEY transfer, and ROOTKEY hierarchical transfer. It supports 16 KLAD software channels. ### Key Derivation Users can generate different keys based on different application scenarios, with the ability to derive up to 232 ROOTKE Ys. The work key derived from the key can be calculated using the provided derivation tool. For usage instructions, refer to "[Key Derivation Tool Description](#ZH-CN_TOPIC_0000002457828277)". ### Plaintext KEY Transfer Plaintext KEY refers to the working key used by the encryption/decryption engine, which is securely stored by the user. - Supports AES 128/192/256 bits encryption/decryption.[¶](#overview-klad-is-the-key-management-module-it-supports-key-derivation-plaintext-key-transfer-and-rootkey-hierarchical-transfer-it-supports-16-klad-software-channels-key-derivation-users-can-generate-different-keys-based-on-different-application-scenarios-with-the-ability-to-derive-up-to-232-rootke-ys-the-work-key-derived-from-the-key-can-be-calculated-using-the-provided-derivation-tool-for-usage-instructions-refer-to-key-derivation-tool-description-plaintext-key-transfer-plaintext-key-refers-to-the-working-key-used-by-the-encryptiondecryption-engine-which-is-securely-stored-by-the-user-supports-aes-128192256-bits-encryptiondecryption "锚链接")

- Supports SM4 128 bits encryption/decryption.
- Hi3403V100 and do not support SM4. ### ROOTKEY Transfer ROOTKEY is the key generated from the root key of the OTP module through key de-obfuscation and key derivation. The ROOTKEY is stored in hardware and is not readable by the user. The working key for encryption/decryption is a KEY obtained after multiple levels of KLAD hierarchical transfer. This KEY is also stored in hardware and is not readable by the user. This scheme is mostly used in scenarios with high security requirements. The OTP root key is securely stored by the user. - Supports AES 128/256 bits encryption/decryption.
- Supports SM4 128 bits encryption/decryption.
- Hi3403V100 and do not support SM4.
- Hi3403V100 and support 2-level KLAD transfer. ### KLAD Usage Notes When KLAD is deployed in different scenarios, its usage may vary. - In the Linux environment - User-mode KLAD can be used by linking the static library libss\_klad.a or the dynamic library libss\_klad.so, depending on libsecurec.a or libsecurec.so. - Kernel-mode KLAD uses module insertion, i.e., insmod ot\_klad.ko, which depends on ot\_osal.ko, ot\_base.ko, sys\_config.ko, and ot\_sys.ko. - In the OPTEE environment - The user-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_tee\_xxx; - The kernel-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_drv\_xxx. - In the UBOOT environment, the user-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_mpi\_xxx. ## Usage Flow ### Plaintext KEY Transfer #### Scenario Description When the working key used for encryption/decryption is provided by the user, the plaintext KEY related interfaces need to be used. KLAD transfers the working key to a KEYSLOT. During encryption/decryption, the encryption/decryption engine retrieves the KEY from the corresponding KEYSLOT for encryption/decryption. #### Workflow The plaintext KEY transfer development steps are as follows: 1. Initialize the KLAD device. Call the interface [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405).
- Create a KLAD handle. Call the interface [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273).
- Bind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510).
- Set KLAD attributes. Call the interface [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393).
- Set the plaintext KEY. Call the interface [ss\_mpi\_klad\_set\_clear\_key](#ZH-CN_TOPIC_0000002457868373).
- Unbind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486).
- Destroy the KLAD handle. Call the interface [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642).
- Deinitialize the KLAD device. Call the interface [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506). #### Notes When using plaintext KEY transfer, please pay special attention to the following points. - The KEYSLOT handle must be created through the CIPHER module during KLAD configuration.
- When transferring a plaintext KEY, the KLAD type must be configured as plaintext KLAD (OT\_KLAD\_TYPE\_CLEARCW). ### ROOTKEY Transfer #### Scenario Description Used in scenarios with high security requirements. The ROOTKEY is generated after key de-obfuscation and key derivation, and after multiple levels of KLAD transfer, a real working key is obtained. The working key is stored in hardware and is not readable by the user. KLAD transfers the working key to a KEYSLOT. During encryption/decryption, the encryption/decryption engine retrieves the KEY from the corresponding KEYSLOT for encryption/decryption. #### Workflow The ROOTKEY transfer development steps are as follows: 1. Initialize the KLAD device. Call the interface [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405).
- Create a KLAD handle. Call the interface [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273).
- Bind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510).
- Set KLAD attributes. Call the interface [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393).
- Set the 1st to (n-1)th level KLAD key information. Call the interface [ss\_mpi\_klad\_set\_session\_key](#ZH-CN_TOPIC_0000002457868369).
- Set the nth level KLAD key information. Call the interface [ss\_mpi\_klad\_set\_content\_key](#ZH-CN_TOPIC_0000002457828237).
- Unbind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486).
- Destroy the KLAD handle. Call the interface [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642).
- Deinitialize the KLAD device. Call the interface [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506). #### Notes When using ROOTKEY transfer, please pay special attention to the following points. - The KEYSLOT handle must be created through the CIPHER module during KLAD configuration.
- When transferring ROOTKEY, the KLAD type must be configured as common KLAD (OT\_KLAD\_TYPE\_COMMON). ## Key Derivation Tool Description The key derivation tool is located in the osdrv/tools/pc/kdf\_customer directory. For usage commands, refer to the readme.txt file in that directory. The following mainly describes the configuration of relevant fields in the key.ini file. **Table 1** key.ini field description

| Field | Meaning |
| --- | --- |
| function | Function. Select 3 (work key). |
| encryption | Algorithm used. Select 0 (AES). |
| oem\_root\_symc\_key | Root key flashed into OTP. |
| protection\_key\_l1 | session\_key, 128 bits. |
| protection\_key\_l2 | content\_key. If 128 bit is used, the derived work\_key is also 128 bit; if 256 bit is used, the derived work\_key is also 256 bit. |
| oem\_rk\_deob\_en | Obfuscation protection. Default is 0. If the relevant OTP has been flashed, it needs to be set to 1. |
| boot\_flag | Whether the work\_key is used during the boot phase. |
| sw\_reg | Derivation material, owner\_id. |

Notes: 1. Except for the fields mentioned above, no other fields need to be modified.
2. If content\_key is 128 bit, work\_key is the first 16 bytes of the generated out.bin file; if content\_key is 256 bit, work\_key is the entire out.bin file generated. # API Reference
KLAD provides the following AP Is: - [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405): Initializes the KLAD module.
- [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506): Deinitializes the KLAD module.
- [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273): Creates a KLAD handle.
- [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642): Destroys an existing KLAD handle.
- [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510): Binds a KLAD handle and a KEYSLOT handle.
- [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486): Unbinds a KLAD handle and a KEYSLOT handle.
- [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393): Sets KLAD attributes.
- [ss\_mpi\_klad\_get\_attr](#ZH-CN_TOPIC_0000002424189662): Gets KLAD attributes.
- [ss\_mpi\_klad\_set\_session\_key](#ZH-CN_TOPIC_0000002457868369): Configures the 1st to (n-1)th level KLAD KEY.
- [ss\_mpi\_klad\_set\_content\_key](#ZH-CN_TOPIC_0000002457828237): Configures the last level KLAD KEY and simultaneously passes the key to KEYSLOT.
- [ss\_mpi\_klad\_set\_clear\_key](#ZH-CN_TOPIC_0000002457868373): Configures a plaintext KEY and simultaneously passes the key to KEYSLOT. ## ss\_mpi\_klad\_init [Description] Initializes the KLAD module. [Syntax] `td_s32 ss_mpi_klad_init(td_void);` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - Supports multiple calls.
- Initialization and deinitialization must be used in pairs. [Example] None. ## ss\_mpi\_klad\_deinit [Description] Deinitializes the KLAD module. [Syntax] `td_s32 ss_mpi_klad_deinit(td_void);` [Parameters] None. [Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - Supports multiple calls.
- Initialization and deinitialization must be used in pairs. [Example] None. ## ss\_mpi\_klad\_create [Description] Creates a KLAD handle. [Syntax] `td_s32 ss_mpi_klad_create (td_handle *klad);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | KLAD handle pointer. | Output |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - klad must not be NULL.
- After using the channel, the corresponding channel should be destroyed.
- Channel creation and destruction must be used in pairs. [Example] None. ## ss\_mpi\_klad\_destroy [Description] Destroys a KLAD. [Syntax] `td_s32 ss_mpi_klad_destroy (td_handle klad);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | KLAD handle. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD handle must have been created.
- Channel creation and destruction must be used in pairs. [Example] None. ## ss\_mpi\_klad\_attach [Description] Binds a KLAD handle and a KEYSLOT handle. [Syntax] `td_s32 ss_mpi_klad_attach(td_handle klad, td_handle target);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | KLAD handle. | Input |
| target | KEYSLOT handle. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD and KEYSLOT handles must have been created. If handles are not created, binding between handles may succeed, but functionality will fail.
- Binding and unbinding must be used in pairs. [Example] None. ## ss\_mpi\_klad\_detach [Description] Unbinds a KLAD handle and a KEYSLOT handle. [Syntax] `td_s32 ss_mpi_klad_detach(td_handle klad, td_handle target);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | KLAD handle. | Input |
| target | KEYSLOT handle. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD and KEYSLOT handles must have been created.
- Binding and unbinding must be used in pairs. [Example] None. ## ss\_mpi\_klad\_set\_attr [Description] Sets KLAD attributes. [Syntax] `td_s32 ss_mpi_klad_set_attr(td_handle klad, const ot_klad_attr *attr);<a name="ss_mpi_klad_set_attr"></a>` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| klad | KLAD handle. | Input |
| attr | KLAD attributes. Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD handle must have been created.
- Can be called multiple times; the last set attributes take effect. [Example] None. ## ss\_mpi\_klad\_get\_attr [Description] Gets KLAD attributes. [Syntax] `td_s32 ss_mpi_klad_get_attr(td_handle klad, ot_klad_attr*attr);<a name="ss_mpi_klad_get_attr"></a>` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| klad | KLAD handle. | Input |
| attr | KLAD attributes. Must not be NULL. | Output |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] The KLAD handle must have been created. [Example] None. ## ss\_mpi\_klad\_set\_session\_key [Description] Configures the 1st to (n-1)th level KLAD KEY. [Syntax] `td_s32 ss_mpi_klad_set_session_key(td_handle klad, const ot_klad_session_key *key);<a name="ss_mpi_klad_set_session_key"></a>` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| klad | KLAD handle. | Input |
| key | 1st to (n-1)th level key configuration. Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD handle must have been created.
- Cannot be called multiple times. [Example] None. ## ss\_mpi\_klad\_set\_content\_key [Description] Configures the last level KLAD KEY and simultaneously passes the key to KEYSLOT. [Syntax] `td_s32 ss_mpi_klad_set_content_key(td_handle klad, const ot_klad_content_key *key);<a name="ss_mpi_klad_set_content_key"></a>` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| klad | KLAD handle. | Input |
| key | Nth level key configuration. Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD handle must have been created.
- Cannot be called multiple times. [Example] None. ## ss\_mpi\_klad\_set\_clear\_key [Description] Configures a plaintext KEY and simultaneously passes the key to KEYSLOT. [Syntax] `td_s32 ss_mpi_klad_set_clear_key(td_handle klad, const ot_klad_clear_key *key);<a name="ss_mpi_klad_set_clear_key"></a>` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| klad | KLAD handle. | Input |
| key | Plaintext KEY configuration. Must not be NULL. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | See [Error Codes](#ZH-CN_TOPIC_0000002424349490). |

[Requirements] - Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
- Library files: libss\_klad.a, libss\_klad.so [Notes] - The KLAD handle must have been created.
- Can be called multiple times; the last set attributes take effect. [Example] None. # Data Types
The relevant data types and data structures are defined as follows (for other common data type definitions, refer to ot\_type.h): - [ot\_klad\_rootkey\_sel](#ZH-CN_TOPIC_0000002424189634): Defines the KLAD ROOTKEY selection enum.
- [ot\_klad\_rootkey\_secure](#ZH-CN_TOPIC_0000002457868397): Defines the KLAD ROOTKEY static value enum.
- [ot\_klad\_rootkey\_attr](#ZH-CN_TOPIC_0000002424189658): Defines the KLAD ROOTKEY attribute structure.
- [ot\_klad\_type](#ZH-CN_TOPIC_0000002457828233): Defines the KLAD type enum.
- [ot\_klad\_cfg](#ZH-CN_TOPIC_0000002424189638): Defines the KLAD configuration information structure.
- [ot\_klad\_crypto\_alg](#ZH-CN_TOPIC_0000002457868381): Defines the algorithm for which the KEY is used in the encryption/decryption engine.
- [ot\_klad\_attr](#ZH-CN_TOPIC_0000002424349482): Defines the KLAD attribute structure.
- [ot\_klad\_alg\_type](#ZH-CN_TOPIC_0000002457868401): Defines the KLAD algorithm type enum.
- [ot\_klad\_level](#ZH-CN_TOPIC_0000002457868385): Defines the KLAD level enum.
- [ot\_klad\_session\_key](#ZH-CN_TOPIC_0000002424349502): Defines the 1st to (n-1)th level KLAD key information structure.
- [ot\_klad\_content\_key](#ZH-CN_TOPIC_0000002424189666): Defines the nth level KLAD key information structure.
- [ot\_klad\_clear\_key](#ZH-CN_TOPIC_0000002457828245): Defines the plaintext key information structure.
- [OT\_KLAD\_MAX\_KEY\_LEN](#ZH-CN_TOPIC_0000002424189646): Defines the KLAD maximum key length. ## ot\_klad\_rootkey\_sel [Description] Defines the KLAD ROOTKEY selection enum. [Definition] `/* klad rootkey select */ typedef enum { OT_KLAD_ROOTKEY_SEL_OEM0 = 0x00, OT_KLAD_ROOTKEY_SEL_OEM1, OT_KLAD_ROOTKEY_SEL_OEM2, OT_KLAD_ROOTKEY_SEL_OEM3, OT_KLAD_ROOTKEY_SEL_VENDOR, OT_KLAD_ROOTKEY_SEL_BUTT, } ot_klad_rootkey_sel;<a name="ot_klad_rootkey_sel"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_ROOTKEY\_SEL\_OEM0 | OTP key management OEM key 0. |
| OT\_KLAD\_ROOTKEY\_SEL\_OEM1 | OTP key management OEM key 1. |
| OT\_KLAD\_ROOTKEY\_SEL\_OEM2 | OTP key management OEM key 2. |
| OT\_KLAD\_ROOTKEY\_SEL\_OEM3 | OTP key management OEM key 3. |
| OT\_KLAD\_ROOTKEY\_SEL\_VENDOR | OTP key management vendor key. |
| OT\_KLAD\_ROOTKEY\_SEL\_BUTT | Boundary value, used for boundary checking. |

[Notes] None. [Related Data Types and Interfaces] - [ot\_klad\_rootkey\_attr](#ot_klad_rootkey_attr)
- [ot\_klad\_cfg](#ot_klad_cfg)
- [ot\_klad\_attr](#ot_klad_attr)
- [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_rootkey\_secure [Description] Defines the KLAD ROOTKEY static value enum. [Definition] `typedef enum { OT_KLAD_ROOTKEY_SEC_REE = 0x00, /* REE key, TEE CPU can select ree key */ OT_KLAD_ROOTKEY_SEC_TEE, /* TEE key, REE CPU can't select tee key */ OT_KLAD_ROOTKEY_SEC_BUTT, } ot_klad_rootkey_secure;<a name="ot_klad_rootkey_secure"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_ROOTKEY\_SEC\_REE | Select REE key static value. |
| OT\_KLAD\_ROOTKEY\_SEC\_TEE | Select TEE key static value. |
| OT\_KLAD\_ROOTKEY\_SEC\_BUTT | Boundary value, used for boundary checking. |

[Notes] - Non-secure CPU cannot select the TEE key static value.
- Secure CPU can select the REE key static value. [Related Data Types and Interfaces] - [ot\_klad\_rootkey\_attr](#ot_klad_rootkey_attr)
- [ot\_klad\_cfg](#ot_klad_cfg)
- [ot\_klad\_attr](#ot_klad_attr)
- [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_rootkey\_attr [Description] Defines the KLAD ROOTKEY attribute structure. [Definition] `/* only OT_KLAD_TYPE_COMMON is valid */ typedef struct { td_u32 owner_id; /* Derivative material, used for mcipher */ ot_klad_rootkey_sel key_sel; /* common klad route select rootkey */ ot_klad_rootkey_secure key_secure; /* Static value select: for ree key or for tee key */
} ot_klad_rootkey_attr;<a name="ot_klad_rootkey_attr"></a>` [Members]

| Member Name | Description |
| --- | --- |
| owner\_id | Derivation material, used for MCIPHER. |
| key\_sel | COMMON KLAD ROOTKEY selection. |
| key\_secure | COMMON KLAD ROOTKEY static value selection. |

[Notes] Only valid when the KLAD type is OT\_KLAD\_TYPE\_COMMON. [Related Data Types and Interfaces] - [ot\_klad\_cfg](#ot_klad_cfg)
- [ot\_klad\_attr](#ot_klad_attr)
- [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_type [Description] Defines the KLAD type enum. [Definition] `/* klad route select */ typedef enum { OT_KLAD_TYPE_CLEARCW, /* Used for clear key */ OT_KLAD_TYPE_COMMON, /* Used for root key */ OT_KLAD_TYPE_BUTT, } ot_klad_type;<a name="ot_klad_type"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_TYPE\_CLEARCW | Plaintext KLAD, used for plaintext KEY. |
| OT\_KLAD\_TYPE\_COMMON | Common KLAD, used for ROOTKEY. |
| OT\_KLAD\_TYPE\_BUTT | Boundary value, used for boundary checking. |

[Notes] None. [Related Data Types and Interfaces] - [ot\_klad\_cfg](#ot_klad_cfg)
- [ot\_klad\_attr](#ot_klad_attr)
- [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_cfg [Description] Defines the KLAD configuration information structure. [Definition] `/* klad config */ typedef struct { ot_klad_type klad_type; /* klad route select: common/clear */ ot_klad_rootkey_attr rootkey_attr; /* rootkey attr, OT_KLAD_TYPE_COMMON is valid */
} ot_klad_cfg;` [Members]

| Member Name | Description |
| --- | --- |
| klad\_type | KLAD type. |
| rootkey\_attr | ROOTKEY attribute configuration. |

[Notes] rootkey\_attr is only valid when the KLAD type is OT\_KLAD\_TYPE\_COMMON. [Related Data Types and Interfaces] - [ot\_klad\_attr](#ot_klad_attr)
- [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_crypto\_alg [Description] Defines the algorithm for which the KEY is used in the encryption/decryption engine. [Definition] `/* The key can be used for which algorithm of the crypto engine. */ typedef enum { OT_KLAD_CRYPTO_ALG_AES = 0, OT_KLAD_CRYPTO_ALG_SM4, OT_KLAD_CRYPTO_ALG_BUTT, } ot_klad_crypto_alg;<a name="ot_klad_crypto_alg"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_CRYPTO\_ALG\_AES | Used for AES algorithm. |
| OT\_KLAD\_CRYPTO\_ALG\_SM4 | Used for SM4 algorithm. |
| OT\_KLAD\_CRYPTO\_ALG\_BUTT | Boundary value, used for boundary checking. |

[Notes] Hi3403V100 and do not support SM4. [Related Data Types and Interfaces] - [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)
- [ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key) ## ot\_klad\_attr [Description] Defines the KLAD attribute structure. [Definition] `/* klad attribute */ typedef struct { ot_klad_cfg klad_cfg;
} ot_klad_attr;<a name="ot_klad_attr"></a>` [Members]

| Member Name | Description |
| --- | --- |
| klad\_cfg | KLAD configuration information. |

[Notes] None. [Related Data Types and Interfaces] - [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
- [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr) ## ot\_klad\_alg\_type [Description] Defines the KLAD algorithm type enum. [Definition] `/* klad algorithm */ typedef enum { OT_KLAD_ALG_TYPE_AES = 0, OT_KLAD_ALG_TYPE_SM4, OT_KLAD_ALG_TYPE_BUTT, } ot_klad_alg_type;<a name="ot_klad_alg_type"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_ALG\_TYPE\_AES | KLAD uses AES algorithm. |
| OT\_KLAD\_ALG\_TYPE\_SM4 | KLAD uses SM4 algorithm. |
| OT\_KLAD\_ALG\_TYPE\_BUTT | Boundary value, used for boundary checking. |

[Notes] Hi3403V100 and do not support SM4. [Related Data Types and Interfaces] - [ot\_klad\_session\_key](#ot_klad_session_key)
- [ot\_klad\_content\_key](#ot_klad_content_key)
- [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)
- [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key) ## ot\_klad\_level [Description] Defines the KLAD level enum. [Definition] `/* klad level */ typedef enum { OT_KLAD_LEVEL1 = 0, OT_KLAD_LEVEL2, OT_KLAD_LEVEL3, OT_KLAD_LEVEL_BUTT, } ot_klad_level;<a name="ot_klad_level"></a>` [Members]

| Member Name | Description |
| --- | --- |
| OT\_KLAD\_LEVEL1 | KLAD level 1. |
| OT\_KLAD\_LEVEL2 | KLAD level 2. |
| OT\_KLAD\_LEVEL3 | KLAD level 3. |
| OT\_KLAD\_LEVEL\_BUTT | Boundary value, used for boundary checking. |

[Notes] Hi3403V100 and support 2-level KLAD. [Related Data Types and Interfaces] - [ot\_klad\_session\_key](#ot_klad_session_key)
- [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key) ## ot\_klad\_session\_key [Description] Defines the 1st to (n-1)th level KLAD key information structure. [Definition] `/* session key: set 1~n-1 stage common route klad */ typedef struct { ot_klad_session_key level; /* klad level */ ot_klad_alg_type alg; /* klad algorithm */ td_u32 key_size; /* klad key size */ td_u8 key[OT_KLAD_MAX_KEY_LEN]; /* klad key */
} ot_klad_session_key;<a name="ot_klad_session_key"></a>` [Members]

| Member Name | Description |
| --- | --- |
| level | Currently configured KLAD level. |
| alg | Algorithm used by KLAD. |
| key\_size | KLAD decryption key length (unit: byte). |
| key | KLAD decryption key. |

[Notes] - key\_size only supports 128 bits, i.e., 16 bytes.
- For Hi3403V100 and , level can only be configured as OT\_KLAD\_LEVEL1. [Related Data Types and Interfaces] [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key) ## ot\_klad\_content\_key [Description] Defines the last level KLAD key information structure. [Definition] `/* content key: set n stage common route klad */
typedef struct { ot_klad_alg_type alg; /* klad algorithm */ ot_klad_crypto_alg crypto_alg; /* allowed target engine algorithm. */ td_u32 key_size; /* klad key size */ td_u8 key[OT_KLAD_MAX_KEY_LEN]; /* klad key */
} ot_klad_content_key;<a name="ot_klad_content_key"></a>` [Members]

| Member Name | Description |
| --- | --- |
| alg | Algorithm used by the current KLAD. |
| crypto\_alg | Algorithm allowed by the encryption/decryption engine. |
| key\_size | KLAD decryption key length (unit: byte), supports 128/256 bits. |
| key | KLAD decryption key. |

[Notes] None. [Related Data Types and Interfaces] [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key) ## ot\_klad\_clear\_key [Description] Defines the plaintext key information structure. [Definition] `/* clear key: set clear route klad */
typedef struct { ot_klad_crypto_alg crypto_alg; /* allowed target engine algorithm. */ td_u32 key_size; /* klad key size */ td_u8 key[OT_KLAD_MAX_KEY_LEN]; /* klad key */
} ot_klad_clear_key;<a name="ot_klad_clear_key"></a>` [Members]

| Member Name | Description |
| --- | --- |
| crypto\_alg | Algorithm allowed by the encryption/decryption engine. |
| key\_size | KLAD decryption key length (unit: byte), supports 128/192/256 bits. |
| key | KLAD decryption key. |

[Notes] None. [Related Data Types and Interfaces] [ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key) ## OT\_KLAD\_MAX\_KEY\_LEN [Description] Defines the KLAD maximum key length. [Definition] ```

# define OT\_KLAD\_MAX\_KEY\_LEN 32[¶](#define-ot_klad_max_key_len-32 "锚链接")

``` [Notes] None. [Related Data Types and Interfaces] - [ot\_klad\_session\_key](#ot_klad_session_key)
- [ot\_klad\_content\_key](#ot_klad_content_key)
- [ot\_klad\_clear\_key](#ot_klad_clear_key)
- [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)
- [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)
- [ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key) # Error Codes
The error codes provided by KLAD are as follows. **Table 1** KLAD module error codes

| Error Code | Macro Definition | Description |
| --- | --- | --- |
| 0x805d0000 | OT\_ERR\_KLAD\_NOT\_INIT | Device not initialized |
| 0x805d0001 | OT\_ERR\_KLAD\_FAILED\_INIT | Device initialization failed |
| 0x805d0002 | OT\_ERR\_KLAD\_NULL\_PTR | NULL pointer in parameters |
| 0x805d0003 | OT\_ERR\_KLAD\_INVALID\_PARAM | Invalid parameter |
| 0x805d0004 | OT\_ERR\_KLAD\_FAILED\_CREATE\_DEV | Failed to create device |
| 0x805d0005 | OT\_ERR\_KLAD\_DEVICE\_BUSY | Device busy |
| 0x805d0006 | OT\_ERR\_KLAD\_FAILED\_SEC\_FUNC | Security function call failed |
| 0x805d0007 | OT\_ERR\_KLAD\_TIMEOUT | Operation timeout |
| 0x805d0008 | OT\_ERR\_KLAD\_FAILED\_MEM | Memory allocation failed |
| 0x805d0009 | OT\_ERR\_KLAD\_FAILED\_OPERATE | KLAD operation failed |
| 0x805d000a | OT\_ERR\_KLAD\_INVALID\_OWNER | Invalid KLAD owner |
| 0x805d000b | OT\_ERR\_KLAD\_INVALID\_HANDLE | Invalid KLAD Handle |

# Acronyms and Abbreviations

| | | |
| --- | --- | --- |
| **K** | | |
| KDF | Key Derivation Function | Key Derivation Function |
| KLAD | Key Ladder | Key Ladder |
| **R** | | |
| REE | Rich Execution Environment | Rich Execution Environment |
| RKP | Root Key Process | Root Key Process |
| **T** | | |
| TEE | Trusted Execution Environment | Trusted Execution Environment |