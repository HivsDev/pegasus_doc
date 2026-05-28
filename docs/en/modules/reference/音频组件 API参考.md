---
title: Audio
---

# Audio

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/音频组件API参考/音频组件 API参考.md
--- # Preface
**Overview** This document is written for programmers developing intelligent analysis solutions using the audio functionality of the media processing chip. It is intended to provide reference information supported by audio during development, including protocol descriptions, AP Is, error codes, etc. **Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |
| V100 |
| V100 |
| V100 |
| V100 |
| V100 |
| V100 |

**Intended Audience** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions** The following symbols may appear in this document, and their meanings are described below.

| Symbol | Description |
| --- | --- |
|  | Indicates a high-level hazard which, if not avoided, will result in death or serious injury. |

**Revision History** The revision history summarizes the changes made in each document update. The latest version of the document includes updates from all previous document versions.

| **Document Version** | **Release Date** | **Change Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First interim version release. |

# Audio Component

## Overview The audio component integrates the AAC codec protocol and provides interfaces to facilitate the integration of third-party codec protocols. Example code for AAC encoding/decoding is located in the sample/audio directory. > **Caution:**[¶](#overview-the-audio-component-integrates-the-aac-codec-protocol-and-provides-interfaces-to-facilitate-the-integration-of-third-party-codec-protocols-example-code-for-aac-encodingdecoding-is-located-in-the-sampleaudio-directory-caution "锚链接")

> If customers need to use AAC format patents, they must obtain authorization from the copyright holder and pay the Licensing Fee. ## Important Concepts - Audio Codec Protocol The encoding/decoding functions provided by the audio component are based on an independently packaged AAC codec library. The core codec operates in user mode and uses CPU software for encoding/decoding. The AAC codec protocol is described in [Table 1](#_Ref224548251). **Table 1** Audio codec protocol description

| Protocol | Sample Rate | Frame Length (samples) | Bitrate (kbps) | Compression Ratio | CPU Consumption | Description |
| --- | --- | --- | --- | --- | --- | --- |
| AAC Encoder | 8k Hz, 16k Hz, 22.05k Hz, 24k Hz, 32k Hz,  44.1k Hz, 48k Hz | - AACLC supports 1024; - EAAC and EAACPLUS support 2048; - AACLD and AACELD support 512. | - | - | 50 M Hz | AAC has undergone two breakthrough technology upgrades:   - aac Plus1 (i.e., EAAC), adds SBR (Spectral Band Replication) technology, enabling the codec to achieve the same audio quality at half the bitrate. - aac Plus2 (i.e., EAACPLUS), adds PS (Parametric Stereo) technology, providing excellent audio quality at low bitrates. aac Plus2 can achieve CD quality at 48 kbit/s. - AAC-LD and AAC-ELD are low-delay voice codec processing solutions. AAC-LD is a public safety industry standard requirement, and AAC-ELD is the encoding format for future communications.   Bitstream ranges and recommended bitrate settings are shown in [Table 2](#_Ref342555172) and [Table 3](#_Ref224621074). |
| AAC Decoder | Compatible with all rates | 512, 1024, 2048 | - | - | 25 M Hz | Backward compatible. Traditional AAC decoders only decode low-frequency information of aac Plus v1 streams, while aac Plus decoders can restore high-frequency information as well. AAC decoders that do not support PS will only obtain mono information when decoding aac Plus v2 streams, while aac Plus2 decoders can produce stereo sound. Note: The decoding mode should use ADEC\_MODE\_STREAM. |

Note: The "CPU consumption" result values are based on an ARM9 288 M Hz environment. 2/2 M Hz indicates that encoding and decoding each consume 2M and 2M CPU, respectively. **Table 2** AAC Encoder bitrate settings for each protocol (bitrate unit: kbps)

| Sample Rate | Channel | LC Bit Rate | | Plus v1 Bit Rate | | Plus v2 Bit Rate | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Supported | Preferred | Supported | Preferred | Supported | Preferred |
| 8k Hz | Mono | 16 to 48 | 24 | -- | -- | -- | -- |
| Stereo | 16 to 96 | 32 | -- | -- | -- | -- |
| 16k Hz | Mono | 24 to 96 | 48 | 24 to 48 | 32 | -- | -- |
| Stereo | 24 to 192 | 48 | 24 to 96 | 32 | 16 to 48 | 32 |
| 22.05k Hz | Mono | 32 to 132 | 64 | 32 to 64 | 48 | -- | -- |
| Stereo | 32 to 265 | 48 | 32 to 128 | 64 | 16 to 64 | 32 |
| 24k Hz | Mono | 32 to 144 | 48 | 32 to 64 | 48 | -- | -- |
| Stereo | 32 to 288 | 48 | 32 to 128 | 64 | 16 to 64 | 32 |
| 32k Hz | Mono | 32 to 192 | 48 | 32 to 64 | 48 | -- | -- |
| Stereo | 32 to 320 | 128 | 32 to 128 | 64 | 16 to 64 | 32 |
| 44.1k Hz | Mono | 48 to 265 | 64 | 32 to 64 | 48 | -- | -- |
| Stereo | 48 to 320 | 128 | 32 to 128 | 64 | 16 to 64 | 48 |
| 48k Hz | Mono | 48 to 288 | 64 | 32 to 64 | 48 | -- | -- |
| Stereo | 48 to 320 | 128 | 32 to 128 | 64 | 16 to 64 | 48 |

Note: "--" indicates this scenario is not supported. **Table 3** AAC Encoder Low Delay protocol bitrate settings (bitrate unit: kbps)

| Sample Rate | Channel | LD Bit Rate | | ELD Bit Rate | |
| --- | --- | --- | --- | --- | --- |
| Supported | Preferred | Supported | Preferred |
| 8k Hz | Mono | 16 to 96 | 24 | 32 to 96 | 32 |
| Stereo | 16 to 192 | 48 |

Note: "--" indicates this scenario is not supported. (remaining AAC Encoder Low Delay bitrate table data continues with similar rows for 16k Hz, 22.05k Hz, 24k Hz, 32k Hz, 44.1k Hz, and 48k Hz sample rates for both Mono and Stereo channels, following the same pattern) ## API Reference The following AP Is in the SDK release package are used for registering and unregistering encoders and decoders. - [ss\_mpi\_aenc\_register\_encoder](#ZH-CN_TOPIC_0000002408115490): Registers an encoder.
- [ss\_mpi\_aenc\_unregister\_encoder](#ZH-CN_TOPIC_0000002441714653): Unregisters an encoder.
- [ss\_mpi\_adec\_register\_decoder](#ZH-CN_TOPIC_0000002408115474): Registers a decoder.
- [ss\_mpi\_adec\_unregister\_decoder](#ZH-CN_TOPIC_0000002408275418): Unregisters a decoder. Registration examples provided in the audio component: - [ss\_mpi\_aenc\_aac\_init](#ZH-CN_TOPIC_0000002408275398): Registers the AAC encoder.
- [ss\_mpi\_adec\_aac\_init](#ZH-CN_TOPIC_0000002441714637): Registers the AAC decoder. ### ss\_mpi\_aenc\_register\_encoder [Description] Registers an encoder. [Syntax] `td_s32 ss_mpi_aenc_register_encoder(td_s32 *handle, const ot_aenc_encoder *encoder);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | Registration handle. | Output |
| encoder | Encoder attribute structure. | Input |

[Return Values]

| Return Value | Description |
| --- | --- |
| 0 | Success. |
| Non-0 | Failed. See [Error Codes](#ZH-CN_TOPIC_0000002408115506). |

[Requirements] - Header files: ot\_comm\_aenc.h, ss\_mpi\_audio.h
- Library file: libss\_mpi.a [Notes] - Users register an encoder with the AENC module by passing the encoder attribute structure, and a registration handle is returned. Users can later unregister the encoder using this handle.
- The AENC module can register up to 20 encoders and already has LPCM, G711a, G711u, G726, and ADPCM encoders pre-registered.
- The same encoding protocol cannot be registered multiple times. For example, if an AAC encoder has already been registered, another AAC encoder cannot be registered.
- Encoder attributes include the encoder type, maximum stream length, encoder name, function pointers for opening the encoder, encoding, and closing the encoder. - Encoder type The SDK uses enums to identify encoding protocols. The corresponding encoder type for the protocol should be selected during registration. - Maximum stream length The maximum length of the encoded stream per frame. The AENC module will allocate memory based on the registered maximum stream length. - Encoder name The encoder name is represented as a string and is used for display in proc information. - Function pointer for opening the encoder A function pointer encapsulated by the SDK, with the prototype: td\_s32 (*func\_open\_encoder)(td\_void \*encoder\_attr, td\_void \*\*encoder); The first parameter is the encoder attribute for passing specific attributes of different encoder types; the second parameter is the encoder handle for returning a handle that can operate the encoder. Both parameters are encapsulated by the user. When encapsulating the second parameter, memory allocation should be considered, as the encoder handle will also be used for encoding and closing the encoder. - Function pointer for encoding A function pointer encapsulated by the SDK, with the prototype: td\_s32 (*func\_enc\_frame)(td\_void \*encoder, const ot\_audio\_frame \*data, td\_u8 \*out\_buf, td\_u32 \*out\_len); The first parameter is the encoder handle returned when the encoder was opened; the second parameter is a pointer to the SDK's audio frame data structure for passing audio frame data; the third parameter is the output buffer pointer; the fourth parameter is the output buffer length. - Function pointer for closing the encoder A function pointer encapsulated by the SDK, with the prototype: td\_s32 (\*func\_close\_encoder)(td\_void \*encoder); The parameter is the encoder handle returned when the encoder was opened. - Users need to encapsulate third-party encoders based on these function prototypes and register them with the AENC module through the encoder attribute structure, thereby integrating third-party encoders.
- The relevant encoder type must be registered before creating an encoding channel. Encoders do not need to be registered repeatedly. [Example] The following code illustrates the registration of an AAC encoder: `td_s32 handle, ret;
aenc_encoder aac; ret = aac_init_enc_lib;
if (ret) { return ret;
} aac.type = OT_PT_AAC;
snprintf(aac.name, sizeof(aac.name), "aac");
aac.max_frame_len = MAX_AAC_MAINBUF_SIZE;
aac.func_open_encoder = open_aac_encoder;
aac.func_enc_frame = encode_aac_frm;
aac.func_close_encoder = close_aac_encoder;
ret = ss_mpi_aenc_register_encoder(&handle, &aac);
if (ret) { return ret;
} return TD_SUCCESS;` [Related Topics] None. ### ss\_mpi\_aenc\_unregister\_encoder [Description] Unregisters an encoder. [Syntax] `td_s32 ss_mpi_aenc_unregister_encoder(td_s32 handle);` [Parameters]

| Parameter Name | Description | Input/Output |
| --- | --- | --- |
| handle | Registration handle (obtained when registering the encoder). | Input |

[Return Values] (Standard return value table - 0 for success, non-0 for failure referring to Error Codes) [Requirements] - Header files: ot\_comm\_aenc.h, ss\_mpi\_audio.h
- Library file: libss\_mpi.a [Notes] Unregistering an encoder is generally not necessary. ### ss\_mpi\_adec\_register\_decoder [Description] Registers a decoder. [Syntax] `td_s32 ss_mpi_adec_register_decoder(td_s32 *handle, const ot_adec_decoder *decoder);` [Parameters] (Standard parameter table - handle is the registration handle output, decoder is the decoder attribute structure input) [Requirements] - Header files: ot\_comm\_adec.h, ss\_mpi\_audio.h
- Library file: libss\_mpi.a [Notes] - Users register a decoder with the ADEC module by passing the decoder attribute structure, and a registration handle is returned.
- The ADEC module can register up to 20 decoders and already has LPCM, G711a, G711u, G726, and ADPCM decoders pre-registered.
- Decoder attributes include the decoder type, decoder name, function pointers for opening the decoder, decoding, getting frame info, and closing the decoder.
- The relevant decoder type must be registered before creating a decoding channel. ### ss\_mpi\_adec\_unregister\_decoder [Description] Unregisters a decoder. Generally not necessary. ### ss\_mpi\_aenc\_aac\_init [Description] Registers the AAC encoder. [Syntax] `td_s32 ss_mpi_aenc_aac_init(td_void);` [Parameters] None. [Requirements] - Source file: audio\_aac\_adp.c
- Header file: audio\_aac\_adp.h
- Library files: libaac\_comm.so, libaac\_enc.so [Notes] This interface is implemented in audio\_aac\_adp.c, which is not packaged as a library. Therefore, when using this interface, audio\_aac\_adp.c and audio\_aac\_adp.h must be included for compilation. These two files are placed in the sample/audio/adp folder by default. Additionally, when SBRENC functionality is needed, the libaac\_sbr\_enc.so library must be added. ### ss\_mpi\_adec\_aac\_init [Description] Registers the AAC decoder. (Similar structure to the encoder init) # Data Types The audio component related data types and data structures are defined as follows: - [ot\_aenc\_encoder](#ZH-CN_TOPIC_0000002408275394): Defines the encoder attribute structure.
- [ot\_adec\_decoder](#ZH-CN_TOPIC_0000002441714629): Defines the decoder attribute structure.
- [ot\_aac\_type](#ZH-CN_TOPIC_0000002441674777): Defines the AAC audio codec protocol type.
- [ot\_aac\_bps](#ZH-CN_TOPIC_0000002408275382): Defines the AAC audio encoding bitrate.
- [ot\_aac\_transport\_type](#ZH-CN_TOPIC_0000002408115466): Defines the AAC audio codec protocol transport encapsulation type.
- [ot\_aenc\_attr\_aac](#ZH-CN_TOPIC_0000002408115470): Defines the AAC encoding protocol attribute structure.
- [ot\_adec\_attr\_aac](#ZH-CN_TOPIC_0000002441714625): Defines the AAC decoding protocol attribute structure. ## ot\_aenc\_encoder [Description] Defines the encoder attribute structure. [Definition] `typedef struct { ot_payload_type type; td_u32 max_frame_len; ot_char name[OT_MAX_ENCODER_NAME_LEN]; td_s32 (*func_open_encoder)(td_void *encoder_attr, td_void **encoder); td_s32 (*func_enc_frame)(td_void *encoder, const ot_audio_frame *data, td_u8 *out_buf, td_u32 *out_len); td_s32 (*func_close_encoder)(td_void *encoder);
} ot_aenc_encoder;` [Members]

| Member Name | Description |
| --- | --- |
| type | Encoding protocol type. See the "System Control" chapter of the "MPP Media Processing Software V5.0 Development Reference". |
| max\_frame\_len | Maximum stream length. |
| name | Encoder name. OT\_MAX\_ENCODER\_NAME\_LEN is defined in the "Audio" chapter of the "MPP Media Processing Software V5.0 Development Reference". |
| func\_open\_encoder | Function pointer for opening the encoder. |
| func\_enc\_frame | Function pointer for encoding. For detailed description, see the "Audio" chapter of the "MPP Media Processing Software V5.0 Development Reference". |
| func\_close\_encoder | Function pointer for closing the encoder. |

## ot\_adec\_decoder [Description] Defines the decoder attribute structure. [Definition] `typedef struct { ot_payload_type type; ot_char name[OT_MAX_DECODER_NAME_LEN]; td_s32 (*func_open_decoder)(td_void *decoder_attr, td_void **decoder); td_s32 (*func_dec_frame)(td_void *decoder, td_u8 **in_buf, td_s32 *left_byte, td_u16 *out_buf, td_u32 *out_len, td_u32 *chns); td_s32 (*func_get_frame_info)(td_void *decoder, td_void *info); td_s32 (*func_close_decoder)(td_void *decoder); td_s32 (*func_reset_decoder)(td_void *decoder);
} ot_adec_decoder;` ## ot\_aac\_type [Description] Defines the AAC audio codec protocol type. [Definition] `typedef enum { OT_AAC_TYPE_AACLC = 0, OT_AAC_TYPE_EAAC = 1, /* eAAC format (also known as HEAAC, AAC+, or aac PlusV1) */ OT_AAC_TYPE_EAACPLUS = 2, /* eAACPLUS format (also known as AAC++ or aac PlusV2) */ OT_AAC_TYPE_AACLD = 3, OT_AAC_TYPE_AACELD = 4, OT_AAC_TYPE_BUTT,
} ot_aac_type;` ## ot\_aac\_bps [Description] Defines the AAC audio encoding bitrate. [Definition] `typedef enum { OT_AAC_BPS_8K = 8000, OT_AAC_BPS_16K = 16000, OT_AAC_BPS_22K = 22000, OT_AAC_BPS_24K = 24000, OT_AAC_BPS_32K = 32000, OT_AAC_BPS_48K = 48000, OT_AAC_BPS_64K = 64000, OT_AAC_BPS_96K = 96000, OT_AAC_BPS_128K = 128000, OT_AAC_BPS_256K = 256000, OT_AAC_BPS_320K = 320000, OT_AAC_BPS_BUTT
} ot_aac_bps;` ## ot\_aac\_transport\_type [Description] Defines the AAC audio codec protocol transport encapsulation type. [Definition] `typedef enum { OT_AAC_TRANSPORT_TYPE_ADTS = 0, OT_AAC_TRANSPORT_TYPE_LOAS = 1, OT_AAC_TRANSPORT_TYPE_LATM_MCP1 = 2, OT_AAC_TRANSPORT_TYPE_BUTT
} ot_aac_transport_type;` [Notes] The LATM1 format does not have a sync frame header mechanism. If stream issues occur, it cannot recover quickly. **Not recommended**. ## ot\_aenc\_attr\_aac [Description] Defines the AAC encoding protocol attribute structure. [Definition] `typedef struct { ot_aac_type aac_type; ot_aac_bps bit_rate; ot_audio_sample_rate sample_rate; ot_audio_bit_width bit_width; ot_audio_snd_mode snd_mode; ot_aac_transport_type transport_type; td_s16 band_width;
} ot_aenc_attr_aac;` ## ot\_adec\_attr\_aac [Description] Defines the AAC decoding protocol attribute structure. [Definition] `typedef struct { ot_aac_transport_type transport_type;
} ot_adec_attr_aac;` # Error Codes ## Audio Encoding Error Codes **Table 1** Audio encoding API error codes

| Error Code | Macro Definition | Description |
| --- | --- | --- |
| 0xa0178001 | OT\_ERR\_AENC\_INVALID\_DEV\_ID | Invalid audio device ID |
| 0xa0178003 | OT\_ERR\_AENC\_INVALID\_CHN\_ID | Invalid audio encoding channel number |
| 0xa0178007 | OT\_ERR\_AENC\_ILLEGAL\_PARAM | Invalid audio encoding parameter |
| 0xa0178008 | OT\_ERR\_AENC\_EXIST | Audio encoding channel already created |
| 0xa0178009 | OT\_ERR\_AENC\_UNEXIST | Audio encoding channel not created |
| 0xa017800a | OT\_ERR\_AENC\_NULL\_PTR | NULL pointer in input parameters |
| 0xa017800b | OT\_ERR\_AENC\_NOT\_CFG | Encoding channel not configured |
| 0xa017800c | OT\_ERR\_AENC\_NOT\_SUPPORT | Operation not supported |
| 0xa017800d | OT\_ERR\_AENC\_NOT\_PERM | Operation not permitted |
| 0xa0178014 | OT\_ERR\_AENC\_NO\_MEM | Insufficient system memory |
| 0xa0178015 | OT\_ERR\_AENC\_NO\_BUF | Encoding channel buffer allocation failed |
| 0xa0178016 | OT\_ERR\_AENC\_BUF\_EMPTY | Encoding channel buffer empty |
| 0xa0178017 | OT\_ERR\_AENC\_BUF\_FULL | Encoding channel buffer full |
| 0xa0178018 | OT\_ERR\_AENC\_NOT\_READY | System not initialized |
| 0xa0178040 | OT\_ERR\_AENC\_ENCODER\_ERR | Audio encoding data error |
| 0xa0178041 | OT\_ERR\_AENC\_VQE\_ERR | AENC VQE processing error |

## Audio Decoding Error Codes (The audio decoding error codes follow a similar pattern with the prefix OT\_ERR\_ADEC\_ and corresponding descriptions.)