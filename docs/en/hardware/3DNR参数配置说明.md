---
title: 3DNR noise reduction
---

# 3DNR noise reduction

title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Hi3403V100╱ 3DNR参数配置说明/Hi3403V100╱ 3DNR参数配置说明.md
--- # Preface
**Product Version** The product versions corresponding to this document are as follows.

| Product Name | Product Version |
| --- | --- |
| Hi3403V100 | V100 |

> **Note:** >This document uses the Hi3403V100 description as an example. Unless otherwise specified, the content for and Hi3403V100 is identical. **Intended Audience** This document (this guide) is primarily intended for the following engineers: - Technical support engineers
> - Software development engineers **Symbol Conventions** The following symbols may appear in this document. Their meanings are as follows.

| **Symbol** | **Description** |
| --- | --- |
| | Indicates a hazard with a high level of risk that, if not avoided, will result in death or serious injury. |

**Modification History**

| **Document Version** | **Release Date** | **Modification Description** |
| --- | --- | --- |
| 00B01 | 2025-09-15 | First temporary version release. |

# Interface and Parameter Description

## Parameter Description of ot\_vpss\_nrx\_v2 The following describes the interfaces and parameters of 3DNR. - [ot\_vpss\_nrx\_v2](#ZH-CN_TOPIC_0000002457840685): defines the parameters of the 3DNR X interface version V2.[¶](#parameter-description-of-ot_vpss_nrx_v2-the-following-describes-the-interfaces-and-parameters-of-3dnr-ot_vpss_nrx_v2-defines-the-parameters-of-the-3dnr-x-interface-version-v2 "锚链接")

- [ot\_vpss\_nrx\_v2\_iey](#ZH-CN_TOPIC_0000002457840633): 3DNR enhancement module parameters.
- [ot\_vpss\_nrx\_v2\_sfy](#ZH-CN_TOPIC_0000002457840665): 3DNR spatial filter parameters.
- [ot\_vpss\_nrx\_v2\_mdy](#ZH-CN_TOPIC_0000002457880749): 3DNR motion detection parameters.
- [ot\_vpss\_nrx\_v2\_tfy](#ZH-CN_TOPIC_0000002424361842): 3DNR temporal filter parameters.
- [ot\_vpss\_nrx\_v2\_nrc0](#ZH-CN_TOPIC_0000002424202038): 3DNR video chroma C0 filter parameters.
- [ot\_vpss\_nrx\_v2\_nrc1](#ZH-CN_TOPIC_0000002424361850): 3DNR video chroma C1 filter parameters. ### ot\_vpss\_nrx\_v2 [Description] Defines the parameters of the 3DNR X interface version V2. [Definition] `typedef struct { ot_vpss_nrx_v2_iey iey[5]; ot_vpss_nrx_v2_sfy sfy[5]; ot_vpss_nrx_v2_mdy mdy[2]; ot_vpss_nrx_v2_tfy tfy[3]; ot_vpss_nrx_v2_nrc0 nrc0; ot_vpss_nrx_v2_nrc1 nrc1; struct { td_u16 limit_range_en : 1; td_u16 nry0_en : 1; td_u16 nry1_en : 1; td_u16 nry2_en : 1; td_u16 nry3_en : 1; td_u16 nrc0_en : 1; td_u16 nrc1_en : 1; td_u16 _rb_ : 9; };` `} ot_vpss_nrx_v2;` [Members]

| Member Name | Description |
| --- | --- |
| iey | Luminance filter enhancement module parameters. |
| sfy | Luminance filter spatial filter parameters. |
| mdy | Luminance filter motion detection parameters. |
| tfy | Luminance filter temporal filter parameters. |
| nrc0 | Chroma filter C0 parameters. |
| nrc1 | Chroma filter C1 parameters. |
| limit\_range\_en | Limit range mode switch. |
| nry0\_en | Luminance filter N0 enable switch. |
| nry1\_en | Luminance filter N1 enable switch. |
| nry2\_en | Luminance filter N2 enable switch. |
| nry3\_en | Luminance filter N3 enable switch. |
| nrc0\_en | Chroma filter C0 enable switch. |
| nrc1\_en | Chroma filter C1 enable switch. |
| \_rb\_ | Reserved. |

### ot\_vpss\_nrx\_v2\_iey [Description] 3DNR enhancement module parameters. [Definition] `typedef struct { td_u8 ies0, ies1, ies2, ies3; td_u16 iedz; } ot_vpss_nrx_v2_iey;` [Members]

| Member Name | Description |
| --- | --- |
| ies0, ies1, ies2, ies3 | Absolute enhancement strength of edges, 0~3 correspond to different frequency bands. Value range: [0, 255]. |
| iedz | Noise control threshold. Not recommended for adjustment, defaults to 0. Value range: [0, 999]. |

[Correspondence between 3DNR X Interface and MPI Interface] - n Xsf6 of N0 corresponds to iey[0].ies0, iey[0].ies1, iey[0].ies2, iey[0].ies3;
- n Xsf6 of N1 corresponds to iey[1].ies0, iey[1].ies1, iey[1].ies2, iey[1].ies3;
- n Xsf6 of N2 corresponds to iey[2].ies0, iey[2].ies1, iey[2].ies2, iey[2].ies3;
- n Xsf6a and n Xsf6b interfaces of N3 - n Xsf6a corresponds to iey[3].ies0, iey[3].ies1, iey[3].ies2, iey[3].ies3; - n Xsf6b corresponds to iey[4].ies0, iey[4].ies1, iey[4].ies2, iey[4].ies3. - iedz for N0~N3 levels is not exposed in the 3DNR X interface. Not recommended for adjustment, defaults to 0. ### ot\_vpss\_nrx\_v2\_sfy [Description] 3DNR spatial filter parameters. [Definition] `typedef struct { struct { td_u16 spn : 4; td_u16 sbn : 4; td_u16 pbr : 5; td_u16 j_mode : 3; }; td_u8 sfr7[4], sbr7[2]; td_u8 sfs1, sbr1; td_u8 sfs2, sft2, sbr2; td_u8 sfs4, sft4, sbr4; struct { td_u16 sth1_0 : 9; td_u16 sf5_md : 1; td_u16 _rb1_ : 6; }; struct { td_u16 sth2_0 : 9; td_u16 sf8_idx0 : 3; td_u16 bri_idx0 : 4; }; struct { td_u16 sth3_0 : 9; td_u16 sf8_idx1 : 3; td_u16 bri_idx1 : 4; }; td_u16 sth1_1, sth2_1, sth3_1; struct { td_u16 sfn0_0 : 4; td_u16 sfn1_0 : 4; td_u16 sfn2_0 : 4; td_u16 sfn3_0 : 4; }; struct { td_u16 sfn0_1 : 4; td_u16 sfn1_1 : 4; td_u16 sfn2_1 : 4; td_u16 sfn3_1 : 4; }; td_u8 sf8_tfr, sf8_thrd, sfr; td_u8 bri_str[OT_VPSS_S_IDX_LEN];
} ot_vpss_nrx_v2_sfy;` [Members]

| Member Name | Description |
| --- | --- |
| j\_mode | Spatial mixing mode. Value range: [0, 4]. |
| spn, sbn | Mixing mode filter selection. Value range: [0, 7]. |
| pbr | Indicates the mixing ratio of the spn and sbn filter results; takes effect when mixing mode j\_mode is 1. Value range: [0, 16]. |
| sfr7 | Indicates the relative strength of the result produced by the filter selected by sbn after blending with spn. Value range: [0, 31]. |
| sfr | Pure spatial filter strength control. Value range: [0, 31]. |
| sfs1, sfs2, sfs4 | Indicates the strength of filters 1~4 (filters 3 and 4 have the same strength). Value range: [0, 255]. |
| sft2, sft4 | Indicates additional strength of filters 2~4. Value range: [0, 255]. |
| sbr1, sbr2, sbr4, sbr7 | Indicates the asymmetric filtering strength of filters 1~4 and 6. sbr1, sbr2, sbr4 value range: [0, 255]. sbr7 value range: [0, 15]. |
| sf5\_md | Indicates the strength of filter 5. Value range: [0, 1]. |
| sth1\_0, sth2\_0, sth3\_0 sth1\_1, sth2\_1, sth3\_1 | Edge preservation thresholds for motion foreground and background regions. The smaller the value, the more edges are preserved, but noise will also be higher. The larger the value, the fewer edges are preserved, with only very strong edges being retained. Value range: [0, 511]. |
| sfn0\_0, sfn1\_0, sfn2\_0, sfn3\_0 sfn0\_1, sfn1\_1, sfn2\_1, sfn3\_1 | Selects different filter types (numbers) based on the sth edge preservation threshold and different image characteristics. Value range: [0, 8]. |
| sf8\_idx0, sf8\_idx1 | Selects the filter numbers used for mixing. Value range: [0, 7]. |
| sf8\_tfr, sf8\_thrd | Upper and lower threshold limits of filter 8, used to determine the mixing ratio. Value range: [0, 255]. |
| bri\_idx0, bri\_idx1 | Selects filters for motion foreground and background respectively, mixed based on luminance. Value range: [0, 8]. |
| bri\_str | Configures the mixing ratio of bri\_idx0, bri\_idx1 with the spatial result based on luminance. OT\_VPSS\_S\_IDX\_LEN defines the maximum configurable number for YUV 3DNR luminance and saturation table debugging, with a value of 17. |
| \_rb1\_ | Reserved. |

[Correspondence between 3DNR X Interface and MPI Interface] - sf8\_idx0, sf8\_idx1, sf8\_tfr, and sf8\_thrd are only valid at the N3 level.
- bri\_idx0, bri\_idx1, and bri\_str are only valid at the N2 and N3 levels.
- sth1\_1, sth2\_1, sth3\_1, sfn0\_1, sfn1\_1, sfn2\_1, and sfn3\_1 are valid at the N0~N2 levels.
- n Xsf1 of N0 corresponds to sfy[0].sfs1, sfy[0].sbr1;
- n Xsf2 of N0 corresponds to sfy[0].sfs2, sfy[0].sft2, sfy[0].sbr2;
- n Xsf4 of N0 corresponds to sfy[0].sfs4, sfy[0].sft4, sfy[0].sbr4;
- n Xsf5 of N0 corresponds to sfy[0].sf5\_md;
- n Xsf7 of N0 corresponds to sfy[0].spn, sfy[0].sbn, sfy[0].pbr, sfy[0].j\_mode;
- n Xsfr7 of N0 corresponds to sfy[0].sfr7[0], sfy[0].sfr7[1], sfy[0].sfr7[2], sfy[0].sfr7[3];
- n Xsbr7 of N0 corresponds to sfy[0].sbr7[0], sfy[0].sbr7[1];
- sfr of N0 corresponds to sfy[0].sfr;
- n Xsfn of N0 corresponds to sfy[0].sfn0\_0, sfy[0].sfn1\_0, sfy[0].sfn2\_0, sfy[0].sfn3\_0;
- n Xsth of N0 corresponds to sfy[0].sth1\_0, sfy[0].sth2\_0, sfy[0].sth3\_0;
- nX2sfn of N0 corresponds to sfy[0].sfn0\_1, sfy[0].sfn1\_1, sfy[0].sfn2\_1, sfy[0].sfn3\_1;
- nX2sth of N0 corresponds to sfy[0].sth1\_1, sfy[0].sth2\_1, sfy[0].sth3\_1.
- n Xsf1 of N1 corresponds to sfy[1].sfs1, sfy[1].sbr1;
- n Xsf2 of N1 corresponds to sfy[1].sfs2, sfy[1].sft2, sfy[1].sbr2;
- n Xsf4 of N1 corresponds to sfy[1].sfs4, sfy[1].sft4, sfy[1].sbr4;
- n Xsf5 of N1 corresponds to sfy[1].sf5\_md;
- n Xsf7 of N1 corresponds to sfy[1].spn, sfy[1].sbn, sfy[1].pbr, sfy[1].j\_mode;
- n Xsfr7 of N1 corresponds to sfy[1].sfr7[0], sfy[1].sfr7[1], sfy[1].sfr7[2], sfy[1].sfr7[3];
- n Xsbr7 of N1 corresponds to sfy[1].sbr7[0], sfy[1].sbr7[1];
- sfr of N1 corresponds to sfy[1].sfr;
- n Xsfn of N1 corresponds to sfy[1].sfn0\_0, sfy[1].sfn1\_0, sfy[1].sfn2\_0, sfy[1].sfn3\_0;
- n Xsth of N1 corresponds to sfy[1].sth1\_0, sfy[1].sth2\_0, sfy[1].sth3\_0;
- nX2sfn of N1 corresponds to sfy[1].sfn0\_1, sfy[1].sfn1\_1, sfy[1].sfn2\_1, sfy[1].sfn3\_1;
- nX2sth of N1 corresponds to sfy[1].sth1\_1, sfy[1].sth2\_1, sfy[1].sth3\_1.
- n Xsf1 of N2 corresponds to sfy[2].sfs1, sfy[2].sbr1;
- n Xsf2 of N2 corresponds to sfy[2].sfs2, sfy[2].sft2, sfy[2].sbr2;
- n Xsf4 of N2 corresponds to sfy[2].sfs4, sfy[2].sft4, sfy[2].sbr4;
- n Xsf5 of N2 corresponds to sfy[2].sf5\_md;
- n Xsf7 of N2 corresponds to sfy[2].spn, sfy[2].sbn, sfy[2].pbr, sfy[2].j\_mode;
- n Xsfr7 of N2 corresponds to sfy[2].sfr7[0], sfy[2].sfr7[1], sfy[2].sfr7[2], sfy[2].sfr7[3];
- sfr of N2 corresponds to sfy[2].sfr;
- n Xsfn of N2 corresponds to sfy[2].sfn0\_0, sfy[2].sfn1\_0, sfy[2].sfn2\_0, sfy[2].sfn3\_0;
- n Xsth of N2 corresponds to sfy[2].sth1\_0, sfy[2].sth2\_0, sfy[2].sth3\_0;
- nX2sfn of N2 corresponds to sfy[2].sfn0\_1, sfy[2].sfn1\_1, sfy[2].sfn2\_1, sfy[2].sfn3\_1;
- nX2sth of N2 corresponds to sfy[2].sth1\_1, sfy[2].sth2\_1, sfy[2].sth3\_1;
- n Xb Idx of N2 corresponds to sfy[2].bri\_idx0, sfy[2].bri\_idx1;
- Table n2bri0 ~ n2bri12 corresponds to sfy[2].bri\_str[OT\_VPSS\_S\_IDX\_LEN];
- n Xsf1 of N3 corresponds to sfy[3].sfs1, sfy[3].sbr1;
- n Xsf2 of N3 corresponds to sfy[3].sfs2, sfy[3].sft2, sfy[3].sbr2;
- n Xsf4 of N3 corresponds to sfy[3].sfs4, sfy[3].sft4, sfy[3].sbr4;
- n Xsf5 of N3 corresponds to sfy[3].sf5\_md;
- sfs6 of N3 corresponds to sfy[4].sfs4, sfy[4].sft4, and sfy[4].sbr4;
- n Xsf7a and n Xsf7b of N3 correspond to sfy[3].spn, sfy[3].sbn, sfy[3].pbr, sfy[3].j\_mode and sfy[4].spn, sfy[4].sbn, sfy[4].pbr, sfy[4].j\_mode respectively;
- n Xsfr7a and n Xsfr7b of N3 correspond to sfy[3].sfr7[0], sfy[3].sfr7[1], sfy[3].sfr7[2], sfy[3].sfr7[3] and sfy[4].sfr7[0], sfy[4].sfr7[1], sfy[4].sfr7[2], sfy[4].sfr7[3] respectively;
- n Xsbr7a and n Xsbr7b of N3 correspond to sfy[3].sbr7[0], sfy[3].sbr7[1] and sfy[4].sbr7[0], sfy[4].sbr7[1] respectively;
- n Xsfna and n Xsfnb of N3 correspond to sfy[3].sfn0\_0, sfy[3].sfn1\_0, sfy[3].sfn2\_0, sfy[3].sfn3\_0 and sfy[4].sfn0\_0, sfy[4].sfn1\_0, sfy[4].sfn2\_0, sfy[4].sfn3\_0 respectively;
- n Xstha and n Xsthb of N3 correspond to sfy[3].sth1\_0, sfy[3].sth2\_0, sfy[3].sth3\_0 and sfy[4].sth1\_0, sfy[4].sth2\_0, sfy[4].sth3\_0 respectively;
- sfr\_a and sfr\_b of N3 correspond to sfy[3].sfr and sfy[4].sfr respectively;
- n Xsf8a and n Xsf8b of N3 correspond to sfy[3].sf8\_idx0, sfy[3].sf8\_idx1, sfy[3].sf8\_tfr, sfy[3].sf8\_thrd and sfy[4].sf8\_idx0, sfy[4].sf8\_idx1, sfy[4].sf8\_tfr, sfy[4].sf8\_thrd respectively;
- n Xb Idx of N3 corresponds to sfy[3].bri\_idx0, sfy[3].bri\_idx1;
- Table n3bri0 ~ n3bri12 corresponds to sfy[3].bri\_str[OT\_VPSS\_S\_IDX\_LEN]; ### ot\_vpss\_nrx\_v2\_mdy [Description] 3DNR motion detection parameters. [Definition] `typedef struct { struct { td_u16 math0 : 10; td_u16 mate0 : 4; td_u16 mai00 : 2; }; struct { td_u16 math1 : 10; td_u16 mate1 : 4; td_u16 mai02 : 2; }; struct { td_u16 adv_math : 1; td_u16 adv_th : 12; td_u16 _rb_ : 3; };
} ot_vpss_nrx_v2_mdy;` [Members]

| Member Name | Description |
| --- | --- |
| mai00, mai02 | Selects which temporal filter and spatial filter to mix. Value range: [0, 3]. |
| math0, math1 | Motion/still decision thresholds for channels 0 and 1. Value range: [0, 999]. |
| mate0, mate1 | Motion detection index for flat areas in channels 0 and 1. Value range: [0, 8]. |
| mabw0, mabw1 | Selection of motion detection window size for channels 0 and 1. Value range: [0, 9]. |
| adv\_math | Enhanced math mode switch. 0: off, 1: on. |
| adv\_th | Controls the effect of enhanced math. Value range: [0, 999]. |
| \_rb\_ | Reserved. |

[Correspondence between 3DNR X Interface and MPI Interface] - adv\_math, adv\_th correspond to the N1 level;
- m Xid, m Xmath, m Xmate, m Xmabw correspond to the N1 and N2 levels.
- m Xid of N1 corresponds to mdy[0].mai00, mdy[0].mai01, mdy[0].mai02;
- m Xmath of N1 corresponds to mdy[0].math0, mdy[0].math1;
- m Xmate of N1 corresponds to mdy[0].mate0, mdy[0].mate1;
- m Xmabw of N1 corresponds to mdy[0].mabw0, mdy[0].mabw1;
- adv Math of N1 corresponds to mdy[0].adv\_math;
- adv Th of N1 corresponds to mdy[0].adv\_th;
- m Xid of N2 corresponds to mdy[1].mai00, mdy[1].mai02;
- m Xmath of N2 corresponds to mdy[1].math0;
- m Xmate of N2 corresponds to mdy[1].mate0;
- m Xmabw of N2 corresponds to mdy[1].mabw0; ### ot\_vpss\_nrx\_v2\_tfy [Description] 3DNR temporal filter parameters. [Definition] `typedef struct { struct { td_u16 tfs0 : 4; td_u16 tdz0 : 10; td_u16 _rb0_ : 2; }; struct { td_u16 tfs1 : 4; td_u16 tdz1 : 10; td_u16 math_mode : 2; }; struct { td_u16 sdz0 : 10; td_u16 str0 : 5; td_u16 ref_en : 1; }; struct { td_u16 sdz1 : 10; td_u16 str1 : 5; td_u16 _rb1_ : 1; }; td_u8 tss0, tss1; td_u16 auto_math; td_u8 tfr0[6], tfr1[6];
} ot_vpss_nrx_v2_tfy;` [Members]

| Member Name | Description |
| --- | --- |
| tfs0, tfs1 | Temporal filter absolute strength for channels 0 and 1. |
| tdz0, tdz1 | Protects texture in motion areas from temporal filtering. Increasing tdz protects texture in motion areas but also weakens the temporal filtering strength. Value range: [0, 999]. |
| str0, str1 | Proportion of the filter result superimposed on the final result for channels 0 and 1. Larger values mean higher proportion. Value range: [0, 31]. |
| tfr0, tfr1 | Relative strength of temporal filtering in still areas for channels 0 and 1. Value range: [0, 31]. |
| tss0, tss1 | Proportion of spatial mixing in temporal still areas for channels 0 and 1. Value range: [0, 15]. |
| ref\_en | Reference frame switch. 0: off 1: on |
| sdz0, sdz1 | Constrains the filter strength for channels 0 and 1. Smaller values mean weaker strength. Value range: [0, 999]. |
| math\_mode | Motion decision mode. Value range: [0, 2]. |
| auto\_math | Motion decision threshold for the 0th level. Value range: [0, 999]. |
| \_rb0\_, \_rb1\_ | Reserved. |

[Correspondence between 3DNR X Interface and MPI Interface] - ref corresponds to tfy[0].ref\_en and tfy[1].ref\_en, used to control the N0 temporal switch and the overall temporal switch respectively.
- n Xstr, n Xsdz, n Xtss, n Xtfs, n Xtfr0, n Xtdz correspond to the N0, N1, and N2 levels; math Mode, auto Math correspond only to the N0 level.
- n Xstr of N0 corresponds to tfy[0].str0;
- n Xsdz of N0 corresponds to tfy[0].sdz0;
- n Xtss of N0 corresponds to tfy[0].tss0;
- n Xtfs of N0 corresponds to tfy[0].tfs0;
- n Xtdz of N0 corresponds to tfy[0].tdz0;
- n Xtfr0 of N0 corresponds to tfy[0].tfr0[0], tfy[0].tfr0[1], tfy[0].tfr0[2], tfy[0].tfr0[3], tfy[0].tfr0[4], tfy[0].tfr0[5];
- math Mode of N0 corresponds to tfy[0].math\_mode;
- auto Math of N0 corresponds to tfy[0].auto\_math.
- n Xstr of N1 corresponds to tfy[1].str0;
- n Xsdz of N1 corresponds to tfy[1].sdz0;
- n Xtss of N1 corresponds to tfy[1].tss0, tfy[1].tss1;
- n Xtfs of N1 corresponds to tfy[1].tfs0, tfy[1].tfs1;
- n Xtdz of N1 corresponds to tfy[1].tdz0, tfy[1].tdz1;
- n Xtfr0 of N1 corresponds to tfy[1].tfr0[0], tfy[1].tfr0[1], tfy[1].tfr0[2], tfy[1].tfr0[3], tfy[1].tfr0[4], tfy[1].tfr0[5];
- n Xtfr1 of N1 corresponds to tfy[1].tfr1[0], tfy[1].tfr1[1], tfy[1].tfr1[2], tfy[1].tfr1[3], tfy[1].tfr1[4], tfy[1].tfr1[5];
- n Xstr of N2 corresponds to tfy[2].str0;
- n Xsdz of N2 corresponds to tfy[2].sdz0;
- n Xtss of N2 corresponds to tfy[2].tss0;
- n Xtfs of N2 corresponds to tfy[2].tfs0;
- n Xtdz of N2 corresponds to tfy[2].tdz0;
- n Xtfr0 of N2 corresponds to tfy[2].tfr0[0], tfy[2].tfr0[1], tfy[2].tfr0[2], tfy[2].tfr0[3], tfy[2].tfr0[4], tfy[2].tfr0[5]; ### ot\_vpss\_nrx\_v2\_nrc0 [Description] 3DNR video chroma filtering C0 parameters. [Definition] `typedef struct { td_u8 sfc; td_u8 sfc_enhance, sfc_ext, trc; struct { td_u16 auto_math : 10; td_u16 tfc : 6; };
} ot_vpss_nrx_v2_nrc0;` [Members]

| Member Name | Description |
| --- | --- |
| sfc | Spatial strength parameter. Value range: [0, 31]. |
| sfc\_enhance | Spatial enhancement strength coarse adjustment parameter. Value range: [0, 255]. |
| sfc\_ext | Spatial enhancement strength fine adjustment parameter. Value range: [0, 255]. |
| trc | Used to suppress color contamination in motion areas. Value range: [0, 255]. |
| tfc | Indicates chroma temporal filtering strength. Value range: [0, 32]. |
| auto\_math | Chroma motion decision threshold. Value range: [0, 999]. |

[Correspondence between 3DNR X Interface and MPI Interface] - sfc corresponds to nrc0.sfc
- tfc corresponds to nrc0.tfc
- trc corresponds to nrc0.trc
- nCmath corresponds to nrc0.auto\_math
- sfcExt corresponds to nrc0.sfc\_enhance and nrc0.sfc\_ext ### ot\_vpss\_nrx\_v2\_nrc1 [Description] 3DNR video chroma filtering C1 parameters. [Definition] `typedef struct { td_u8 sfs1, sbr1; td_u8 sfs2, sft2, sbr2; td_u8 sfs4, sft4, sbr4; td_u8 sfc6, sfc_ext6; struct { td_u8 sfr6_u : 4; td_u8 sfr6_v : 4; }; struct { td_u16 sf5_str_u : 5; td_u16 sf5_str_v : 5; td_u16 post_sfc : 5; td_u16 _rb0_ : 1; }; struct { td_u16 spn0 : 3; td_u16 sbn0 : 3; td_u16 pbr0 : 4; td_u16 spn1 : 3; td_u16 sbn1 : 3; }; struct { td_u8 pbr1 : 4; td_u8 _rb1_ : 4; }; struct { td_u8 sat0_l_sfn8 : 4; td_u8 sat1_l_sfn8 : 4; }; struct { td_u8 sat0_h_sfn8 : 4; td_u8 sat1_h_sfn8 : 4; }; struct { td_u8 hue0_l_sfn9 : 4; td_u8 hue1_l_sfn9 : 4; }; struct { td_u8 hue0_h_sfn9 : 4; td_u8 hue1_h_sfn9 : 4; }; struct { td_u8 bri0_l_sfn10 : 4; td_u8 bri1_l_sfn10 : 4; }; struct { td_u8 bri0_h_sfn10 : 4; td_u8 bri1_h_sfn10 : 4; }; struct { td_u8 sfn0 : 4; td_u8 sfn1 : 4; }; td_u8 bak_grd_sat[OT_VPSS_S_IDX_LEN], for_grd_sat[OT_VPSS_S_IDX_LEN]; td_u8 bak_grd_hue[OT_VPSS_S_IDX_LEN], for_grd_hue[OT_VPSS_S_IDX_LEN]; td_u8 bak_grd_bri[OT_VPSS_S_IDX_LEN], for_grd_bri[OT_VPSS_S_IDX_LEN];
} ot_vpss_nrx_v2_nrc1;` [Members]

| Member Name | Description |
| --- | --- |
| sfs1, sfs2, sfs4 | Indicates the strength of filters 1~4 (filters 3 and 4 have the same strength). Value range: [0, 255]. |
| sft2, sft4 | Indicates additional strength of filters 2~4. Value range: [0, 255]. |
| sbr1, sbr2, sbr4 | Indicates the asymmetric filtering strength of filters 1~4 and 6. Value range: [0, 255]. |
| sf5\_str\_u, sf5\_str\_v | Filtering strength of filter 5 (large window) for U and V components respectively. Value range: [0, 31]. |
| sfc6, sfc\_ext6 | Coarse adjustment strength and fine adjustment strength of filter 6. Value range: [0, 255]. |
| sfr6\_u, sfr6\_v | Strength of filter 6 applied to U and V components. Value range: [0, 15]. |
| spn0, sbn0, pbr0 spn1, sbn1, pbr1 | spn0, sbn0 and spn1, sbn1 select mixing filters for the motion foreground and background regions respectively. Value range: [0, 6]. pbr0 and pbr1 indicate the mixing ratios for the motion foreground and background respectively. Value range: [0, 15]. |
| sat0\_l\_sfn8, sat0\_h\_sfn8 sat1\_l\_sfn8, sat1\_h\_sfn8 | Selects filters for mixing based on saturation. sat0 and sat1 act on motion foreground and background respectively. Value range: [0, 7]. |
| hue0\_l\_sfn9, hue0\_h\_sfn9 hue1\_l\_sfn9, hue1\_h\_sfn9 | Selects filters for mixing based on hue. hue0 and hue1 act on motion foreground and background respectively. Value range: [0, 8]. |
| bri0\_l\_sfn10, bri0\_h\_sfn10 bri1\_l\_sfn10, bri1\_h\_sfn10 | Selects filters for mixing based on brightness. bri0 and bri1 act on motion foreground and background respectively. Value range: [0, 9]. |
| sfn0, sfn1 | Indicates mixing filters acting on the motion foreground and background. |
| bak\_grd\_sat for\_grd\_sat | Configure mixing ratio based on saturation (acting on foreground and background respectively). Value range: [0, 255]. |
| bak\_grd\_hue for\_grd\_hue | Configure mixing ratio based on hue (acting on foreground and background respectively). Value range: [0, 255]. |
| bak\_grd\_bri for\_grd\_bri | Configure mixing ratio based on brightness (acting on foreground and background respectively). Value range: [0, 255]. |

[Correspondence between 3DNR X Interface and MPI Interface] - n Csf1 corresponds to nrc1.sfs1 and nrc1.sbr1;
- n Csf2 corresponds to nrc1.sfs2, nrc1.sft2, and nrc1.sbr2;
- n Csf4 corresponds to nrc1.sfs4, nrc1.sft4, and nrc1.sbr4;
- nCsf5u corresponds to nrc1.sf5\_str\_u;
- nCsf5v corresponds to nrc1.sf5\_str\_v;
- n Csfc6 corresponds to nrc1.sfc6 and nrc1.sfc\_ext6;
- nCsf6uv corresponds to nrc1.sfr6\_u and nrc1.sfr6\_v;
- nC Xsf7 corresponds to nrc1.spn0, nrc1.sbn0, nrc1.pbr0, nrc1.spn1, nrc1.sbn1, and nrc1.pbr1;
- nCXsf8 corresponds to nrc1.sat0\_l\_sfn8, nrc1.sat0\_h\_sfn8, nrc1.sat1\_l\_sfn8, and nrc1.sat1\_h\_sfn8;
- nCXsf9 corresponds to nrc1.hue0\_l\_sfn9, nrc1.hue0\_h\_sfn9, nrc1.hue1\_l\_sfn9, and nrc1.hue1\_h\_sfn9;
- nCXsf10 corresponds to nrc1.bri0\_l\_sfn10, nrc1.bri0\_h\_sfn10, nrc1.bri1\_l\_sfn10, and nrc1.bri1\_h\_sfn10;
- n Csfn corresponds to nrc1.sfn0 and nrc1.sfn1;
- Table c0sat0~c0sat12 corresponds to for\_grd\_sat[OT\_VPSS\_S\_IDX\_LEN];
- Table c1sat0~c1sat12 corresponds to bak\_grd\_sat[OT\_VPSS\_S\_IDX\_LEN];
- Table c0hue0~c0hue12 corresponds to for\_grd\_hue[OT\_VPSS\_S\_IDX\_LEN];
- Table c1hue0~c1hue12 corresponds to bak\_grd\_hue[OT\_VPSS\_S\_IDX\_LEN];
- Table c0bri0~c0bri12 corresponds to for\_grd\_bri[OT\_VPSS\_S\_IDX\_LEN];
- Table c1bri0~c1bri12 corresponds to bak\_grd\_bri[OT\_VPSS\_S\_IDX\_LEN]; **Note: For parameters in the MPI interface that do not correspond to the debug interface, it is recommended to set the default value to 0.** ## Default Parameters The default interface parameters for Hi3403V100 YUV 3DNR parameters are shown in [Figure 1](#ref515453020). **Figure 1** 3DNR parameter interface parameter screen  The luminance denoising (N Ry) of 3DNR consists of four series-connected denoising functions, divided into 4 levels numbered N0, N1, N2, N3. Due to implementation differences, series effects, etc., filters of the same number and type at different levels may not produce completely identical results. N0~N2 can select temporal filtering and spatial filtering. N3 is a pure spatial filter (with temporal assistance). The color filter is independent of the luminance filter, divided into two levels, C1 and C2, as shown in [Figure 2](#ref515443368). **Figure 2** 3DNR parameter numbering diagram 

> **Note:** >- The X in nX\*\* and mX\*\* parameters represents the level number, referring to the nth level. For example, n0sf2 specifically refers to the N0 level parameter in the n Xsf2 series parameters, and m1id0 specifically refers to the first-level parameter in the m Xid0 series.
> - [en] enables the denoising function for that level. 0 indicates the function at this level is off, 1 indicates the function is active. Parameters marked in red font are parameters not recommended for adjustment.
> - The N3 spatial filter parameters [n Xsf6], [n Xsf7], [n Xsfr7], [n Xsbr7], [n Xsf8], [n Xsfn], [n Xsth], and [sfr] each have two sets of interfaces (as shown in the N3a and N3b areas in [Figure 2](#ref515443368)), acting on the motion area (N3a) and the still area (N3b) to achieve different processing effects. For the N3 level to take effect, the N2 level must be enabled with temporal reference turned on; otherwise, N3 has no practical effect.
> - Chroma is divided into two levels, C0 and C2, controlled by the nC0en and nC1en switches respectively. [n Csfc6], [n Csfc6uv], [nC Xsf7], [nC Xsf8], [nC Xsf9], and [nC Xsf10] each have two sets of interfaces (as shown in the C3a and C3b areas in [Figure 2](#ref515443368)), acting on the motion area (C3a) and the still area (C3b) to achieve different processing effects.
> - Area F is the table area. # Interface Spatial Filter Parameter Description
> Spatial filtering includes basic filters 0 to 5, namely n Xsf0, n Xsf1, n Xsf2, n Xsf3, n Xsf4, sfs5. Different levels use different types of spatial filters. N0 and N1 use filters with stronger denoising and edge-preserving capabilities, but are prone to banding noise (referred to as the S Fi filter bank). N2 and N3 use filters with slightly weaker denoising and edge-preserving capabilities but have fewer side effects (referred to as the S Fk filter bank). (Note: The S Fi and S Fk filter bank parameters have basically the same functions, but due to differences in filter characteristics, they perform differently in denoising. The X in the nX\*\* parameters represents the level number, referring to the nth level.) - **[n Xsf1] [n Xsf2] [n Xsf4]** Used for debugging filter 1, filter 2, and filter 4 (three spatial filters with different characteristics) respectively. - Filters 1 and 2 are characterized by strong denoising for strong image edges but weaker denoising for flat areas (compared to filter 4, flat areas have more graininess). - Filter 4 is characterized by strong denoising for flat areas, effectively removing graininess from flat areas. It has strong edge preservation (sharper strong edges), but relatively weaker edge denoising. - In the N2 S Fk filter bank, filters 1 and 2 share the same strength parameter (parameter 2). - Each level's [n Xsf1] has two parameters: sfs and sbr in sequence. [n Xsf2] and [n Xsf4] interfaces have three parameters: sfs, sft, and sbr in sequence. - The sfs parameter adjusts filter strength, range: [0, 255]. The sft parameter supplements the filter strength. Normally, only sfs needs to be adjusted (sft set to 0). However, when sfs is set large and additional denoising strength is needed, sft can be adjusted as a supplement. - The sbr parameter is used to debug the "bright/dark asymmetric" denoising mode: set to 128 for symmetrical light/dark denoising mode (default mode); set to less than 128 to favor bright noise removal; set to greater than 128 to favor dark noise removal. The larger the deviation from 128, the greater the asymmetry. Value range: [0, 255]. - **[n Xsf0, n Xsf3]** Two non-explicitly adjustable filters: filter 0 and filter 3. - Filter 0 is the original input pixel for that level. - Filter 3 has an effect between filters 2 and 4. - n Xsf3 shares the same configuration parameters as n Xsf4. - **[sfs5]** Filter 5 is used to remove large-grain noise. Filter strength range: [0, 1]. A value of 1 gives stronger strength but may lose more detail.
> - **[n Xsf6]**: This interface is used to debug filter 6, which is the mixed result of filters 1 to 5, used for combining denoising or detail enhancement across different frequency bands. The four parameters configure four groups of filter results respectively. The first parameter configures the result of filter 1, and so on. - When a parameter for a given filter in the [n Xsf6] interface is less than 64, that filter result is used for denoising — the smaller the value, the stronger the denoising. - When the parameter is greater than 64, the filter result is used for detail enhancement — the larger the value, the stronger the enhancement. - When the parameter equals 64, it effectively disables that filter's influence on the final combined result. Value range: [0, 255]. - The final output of this interface is the mixed result of four groups of filters. If the average of the four parameters is greater than 64, the final output leans toward enhancement; if less than 64, it leans toward denoising. - This interface has a constraint: for all values less than 64, the sum of their distances to 64 must be less than 64. - **[sfs6]** This interface is used at the N3 level to set the strength of the four filter groups in filter 6. The three parameters are sfs, sft, and sbr in sequence (see the [n Xsf1] [n Xsf2] [n Xsf4] interface for their meanings). Value range: [0, 255].
> - **[n Xsf7]** This interface configures the result of filter 7, which is the mixed result of two filter groups. The four parameters of this interface are spn, sbn, pbr, and j\_mode in sequence. spn and sbn are the filter numbers to participate in mixing (selectable from filters 0 to 6). j\_mode is the mixing mode, value range: [0, 4]. When this parameter is 0, the output is the original value. Other values represent four different mixing modes: Mode 1 is proportional mixing, with the mixing weight determined by pbr (value range: [0, 15]); the larger the mixing weight, the more it favors the result of the sbn filter. When the value is 2~4, the mixing method outputs the sbn filter result but tends toward the result of the first filter spn. - **[n Xsfr7]** This interface takes effect when j\_mode of the [nXsf7] interface is selected as 4. It is used for the four checking mechanisms constrained by this mode. The larger the value, the more it favors selecting sbn of [n Xsf7]. Value range: [0, 31]. The final result is the value closest to sbn among the four methods.
> - **[n Xsbr7]** This interface is used for the bright/dark asymmetric adjustment of filter 7. This parameter only takes effect when j\_mode of [nXsf7] is selected as 4. The two parameters control the mixing proportions of spn and sbn in [n Xsf7] respectively, allowing different mixing proportions for bright and dark results.
> - **[n Xsf8]** This interface configures filter 8, which is the mixed result of two filter groups based on image texture features. The four parameters are sf8\_idx0, sf8\_idx1, sf8\_thrd, and sf8\_tfr in sequence. The first two parameters, sf8\_idx0 and sf8\_idx1, are the filter numbers to participate in mixing (selectable from filters 0 to 7). The last two parameters, sf8\_tfr and sf8\_thrd, are the mixing thresholds (upper limit and lower limit respectively). The mixing method is as follows: - When the characteristic value is less than the lower threshold sf8\_thrd, output the result of sf8\_idx1. - When the characteristic value is greater than the upper threshold sf8\_tfr, output the result of sf8\_idx0. - Otherwise, output the mixed result of sf8\_idx0 and sf8\_idx1. Note: Only the third parameter in the [n3sfn] and [n4sfn] interfaces can configure the use of filter 8. sf8\_tfr should be set greater than or equal to sf8\_thrd. - **[n Xsfn/nX2sfn] [n Xsth/nX2sth]**: [n Xsfn/nX2sfn] selects different filter types for different image characteristic areas, with values [0, 8]. It is used in conjunction with the [n Xsth/nX2sth] interface. n Xsth/nX2sth specifies the upper and lower characteristic discrimination thresholds for different areas, with values [0, 511]. n Xsfn, n Xsth and nX2sfn, nX2sth in the N0~N2 levels correspond to the selection of filters and thresholds for the foreground and background respectively. **Note: Background filtering depends on temporal domain being enabled. If using pure spatial mode, nX2sfn and nX2sth will not take effect, and the strength is also determined by the [n Xtss] interface. The larger this interface value, the stronger the background filtering strength.** The n Xsfn/n Xsth parameters are sfn0, sfn1, sfn2, sfn3 and sth1, sth2, sth3 respectively, mixed as follows: - When the third characteristic is less than sth3, select the sfn3 result. - When it is greater than or equal to sth3 and the second characteristic is less than sth2, select the sfn2 result. - When it is greater than or equal to sth2 and the first characteristic is less than sth1, select the sfn1 result. - When the first characteristic is greater than sth1, select the sfn0 result. This method enables different processing effects in different areas. sth1, sth2, and sth3 use characteristic thresholds of different filters, and the metrics differ, so they cannot be directly compared. - **[sfr]** Controls the overall spatial filtering result. Values: [0, 31]. Larger values mean stronger spatial action. When N is 0, spatial filtering is off. This interface only takes effect after ref is enabled.
> - **[n Xb Idx]** Used to select a result from filters 0~8 and mix it with the spatial result based on image brightness. The two parameters of this interface correspond to foreground and background denoising respectively (N3 level has only one parameter, shared by foreground and background). The mixing ratio can be determined from the SFY\_BRI table. The horizontal axis of the table represents the brightness index, and the vertical axis represents the mixing ratio. The higher the ratio, the more the result tends toward the filter selected by this interface. # Temporal Interface Parameter Description
> Each level includes temporal information for image processing. The temporal domain at the N1 level can use a hierarchical processing structure (layer 0 and layer 1), where each temporal interface has two sets corresponding to the two layers (if the interface has multiple parameters, the suffixes 0 and 1 are used to distinguish layers, e.g., n Xtfr0, n Xtfr1). For recorder applications, it is generally recommended to use hierarchical processing, setting layer 1 as the background layer and layer 0 as the foreground layer for separate processing. The other three levels use a single-layer structure, where the N3 level uses a spatial processing approach that leverages temporal information. - **[ref]**: This interface represents the reference frame switch. The N1 ref is the overall temporal reference switch. When set to 0, the reference frame is not loaded and temporal filtering is invalid. When set to 1, temporal filtering parameters can take effect. When N0 ref is 1, the N0 level can use the reference frame for temporal filtering. **Note**: Only in black-and-white fusion scenes, when BNR temporal and VB's OT\_VB\_SUPPLEMENT\_BNR\_MOT\_MASK are enabled, can N0 ref and math Mode be set to 1 (but the VI module cannot have mirror or crop operations). In other scenes, N0 ref and math Mode are disabled by default.
> - **[n Xstr]**: Spatiotemporal filtering to reduce noise, but may introduce some veiling noise. Larger values provide better denoising but increase the probability of veiling noise. Values: [0, 31]. For recorder applications, it is generally recommended to use the default value and not adjust this parameter. - **[n Xsdz]**: Used to limit the spatial filter corresponding to the n Xstr interface. Values: [0, 999]. Smaller values make n Xstr more effective. A value of 999 effectively disables the spatial filter at that level. For recorder applications, it is generally recommended to use the default value and not adjust this parameter.
> - **[n Xtss]**: Larger values make the still area smoother, but the still area image content may become blurrier. Value range: [0, 15]. The two values of this parameter act on different regions. - If not using partitioned processing mode, adjusting this parameter can smooth the background. - If using partitioned processing mode, the first parameter can be appropriately increased to act on areas with relatively less motion to prevent foreground blurring. The second parameter acts on the background. - **[n Xtfs]**: Temporal filtering strength. When the current filter area uses temporal filtering, this parameter represents the temporal action strength. Larger values mean stronger strength. Value range: [0, 15].
> - **[n Xtfr]**: Smear/denoising balance control parameter. There are 6 processing methods total. Smaller values reduce smear but also weaken the denoising capability. The result selects the one with the most obvious denoising effect among the 6 methods. Value range: [0, 31].
> - **[n Xtdz]**: Used to protect texture. Increasing tdz protects texture in motion areas but also weakens the denoising effect. Value range: [0, 999].
> - **[m Xmath]**: Motion/still decision threshold. Larger values result in more pixels being judged as "still" by the motion detection unit, thus more pixels undergo temporal filtering, making the image quieter. Generally, set TFS to maximum, then adjust m Xmath until the rain-like noise is just suppressed, then appropriately lower TFS until there is no rain-like noise. The N1 level uses hierarchical application. The system first uses the second value of this interface to divide the still area of the image as the image's background layer (i.e., the absolutely still area). The remaining image, as the foreground layer, will be further divided into relatively still and motion areas based on the first parameter for separate processing.
> - **[auto Math]**: N0 motion decision threshold. Similar definition to the [m Xmath] interface. Value range: [0, 999]. Recommended debugging value: around 128.
> - **[math Mode]**: Motion decision mode. Value range: [0, 1]. - When set to 0, N0's motion decision [auto Math] is invalid, resulting in a pure temporal effect, with smear-prone motion areas. - When set to 1, N0's motion decision is enabled. Still areas have temporal effects. [auto Math] can be adjusted to control smear in motion areas. - **[m Xid]**: Divides areas based on the [m Xmath] result and selects the output effect. Each parameter takes values [0, 3], representing the output results of [sfr], [n Xstr], [n Xtfr], [n Xtfs] respectively. Larger values mean stronger temporal parameter action. - The first parameter of this interface corresponds to the processing selection for areas judged as motion (characteristic greater than or equal to math). It is recommended to select between 0 and 1. - The second parameter corresponds to the processing selection for areas judged as still (characteristic less than math). It is recommended to select between 2 and 3. - For first-level hierarchical processing, the m Xid interface is used to debug the effect of the foreground layer. - **[Adv Math]** Switch for selecting between the standard motion decision interface and the enhanced motion decision interface. It is recommended to turn on this switch for hierarchical processing. The enhanced mode only acts on the foreground layer of the first level. When using the enhanced interface, the math value set for the foreground layer is usually smaller than that of the standard interface. Value range: [0, 1]. 0 for standard mode, 1 for enhanced mode. If not using zoning, set this interface to 0.
> - **[Adv Th]** This interface determines the action strength of the enhanced math. Smaller values mean stronger action.
> - **[m Xmate]**: Flat area motion detection index. Larger values result in more pixels being judged as "still" by the flat motion detection unit, thus more pixels undergo temporal filtering, making the image quieter. Generally, first adjust math to an appropriate level, then fine-tune mate to balance rain-like noise and motion smear. Value range: [0, 8].
> - **[m Xmabw]**: Selection of motion detection window size. Primarily used with math. Larger values mean larger windows. When rain-like noise cannot be suppressed even with a large math value under low illumination, it is recommended to adjust mabw above 7 to relieve the burden on math for noise suppression and reduce the side effects of temporal filtering. Value range: [0, 9]. For N1 level hierarchical processing, the background layer (layer 1) mabw range: [5, 9]; the foreground layer (layer 0) range: [0, 9], but [0, 4] is recommended to prevent smear. N2 level is not layered; mabw range: [5, 9]. # Chroma Denoising Parameter Description
> Chroma denoising is divided into two levels: N Rc0 and N Rc1, controlled by the nC0en and nC1en switches respectively. N Rc0 is spatiotemporal processing; N Rc1 is spatial processing with temporal assistance. N Rc0 parameter interface: - **[n Cmath]**: Chroma motion decision threshold. Similar definition to the [auto Math] interface. Value range: [0, 999]. Recommended debugging value: around 128. In the following cases, this interface is set to 999 by default (note: C1 chroma parameters will not distinguish between foreground and background at this time): - N1 temporal is disabled or BNR temporal is disabled. - VI module has crop, scaling, or LDC operations. - Block-partitioned scenes. - VB's OT\_VB\_SUPPLEMENT\_BNR\_MOT\_MASK is not enabled. - **[sfc]**: Spatial filtering strength. Value range: [0, 31].
> - **[sfc Ext]**: Additional strength of the sfc spatial filter, further increasing filtering strength based on sfc results. Both interfaces of this parameter indicate the filtering strength magnitude. Value range: [0, 255]. The first parameter is coarse adjustment strength, the second is fine adjustment strength. The larger the parameter adjustment, the stronger the filtering, but it easily causes loss of highly saturated colors. Recommended for appropriate use under low illumination.
> - **[tfc]**: When n Cmath is 999, this interface takes effect. Indicates chroma temporal filtering strength. It is generally recommended that tfc be adjusted no more than 15 under low illumination, otherwise side effects such as color smear may occur. Value range: [0, 32]. - **[trc]**: When n Cmath is 999, this interface takes effect. Value range: [0, 255]. Used to suppress color noise in motion areas, but increasing the parameter easily causes color contamination. When color contamination occurs, adjust **trc** to within 10. N Rc1 parameter interface: Spatial filtering in N Rc1 includes basic filters 0 to 6, corresponding to interfaces n Csf0, n Csf1, n Csf4, n Csf5u, n Csf5v, n Csfc6, n Csfc6. Others are mixing filter interfaces, each divided into two groups for processing the motion foreground and background of the image. - **[n Csf1] [n Csf2] [n Csf4]** Used for debugging filter 1, filter 2, and filter 4 (three spatial filters with different characteristics). Same definition as the luminance interfaces [n Xsf1] [n Xsf2] [n Xsf4].
> - **[n Csf5u] [n Csf5v]** Filter 5 parameter indicates filtering strength. Value range: [0, 31]. Acts on the chroma UV components respectively. Primarily removes low-frequency color noise but easily loses color. Recommended for medium-to-low illumination use.
> - **[n Csfc6]** Additional filtering strength based on filter 4. Both interfaces of this parameter indicate the filtering strength magnitude. Value range: [0, 255]. The first parameter is coarse adjustment strength, the second is fine adjustment strength. Effect is similar to the [sfc Ext] interface.
> - **[n Csfc6uv]** The two parameters of this interface control the filtering strength of filter 6 on the UV components respectively. Value range: [0, 15]. Larger values mean stronger filtering.
> - **[n Csf7]** Chroma mixing filter. The first and second parameters of the two parameter groups (3 each on the left and right) of this interface indicate the filters to be mixed (selectable from filters 0 to 6). The third parameter indicates the mixing ratio. Value range: [0, 15]. Larger values make the result lean more toward the first parameter's result.
> - **[n Csf8] [n Csf9] [n Csf10]** Mixing filters based on saturation, hue, and brightness respectively. The two parameters of the two groups (2 each on the left and right) of this interface indicate the filters to be mixed for mixing. The mixing ratio is determined from the SAT, HUE, and BRI tables. The horizontal axis represents the chroma, saturation, and brightness indices, and the vertical axis represents the mixing ratio. Higher ratios tend toward the result of the second filter.
> - **[n Csfn]** The two parameters of this interface select the effective filters for foreground and background respectively. Value range: [0, 10].
> - **[post SFC]** Spatial filter acting on the final result. Parameter is filter strength. Value: [0, 31]. Generates the final effect. This filter does not distinguish between foreground and background. # 3DNR Interface Debugging Guide for Typical Scenarios

## Typical Non-Face Capture Recorder Application Scenarios Similar to previous chip tuning, the focus is on temporal denoising, with spatial denoising as a supplement. The main difference compared to before is that the 0th level of luminance denoising and chroma denoising supports temporal processing and can be coordinated with BNR for motion/still decision and temporal noise reduction debugging. 1. It is recommended to enable the N0 reference frame, set math Mode to 1, and set auto Math to around 128. Appropriately debug the BNR temporal parameters tfs and tfr, in coordination with the overall temporal intensity, to suppress rain-like noise in the background image. Then, adjust the temporal denoising parameters of the middle two levels, including m Xtfs, m Xmath, m Xmabw, m Xmate. - Layers 0 and 1 of N1 can serve as the foreground and background layers respectively. Tune m1math of the background layer to suppress rain-like noise in the background image as appropriate. Then tune m1math of the foreground layer to control some foreground motion noise. - Tune n1tfs of the first level to suppress the overall noise level of the image as appropriate, balancing the temporal denoising effect and motion smear. Generally, tfs of the foreground layer should be set smaller than that of the background to prevent motion object smear. - Tune m2math and n2tfs of the second level to control the overall quietness level and amplitude of the noise. m2math of the second level is usually set smaller than m1math of the first level to prevent smear. - Under low illumination, to relieve the burden on math, the mabw parameter can be appropriately adjusted. Under extremely low illumination, the mate parameter can be appropriately adjusted to suppress overall image noise. For hierarchical mode, the foreground layer's mabw window is recommended to use small windows 0~4. If using Adv Math mode, the foreground layer's mabw window can only be 4. - For the spatial filter types of the middle two levels, it is recommended to use filter 6 uniformly. However, the first level should increase the weight of filter 2 to favor denoising capability, sacrificing some edge preservation ability. The second level should increase the weight of filter 4 to favor edge preservation, removing noise in non-edge areas. - For the hierarchical mode of the first level, the foreground layer's n1tss can be increased to mix a certain proportion of spatial filtering results into the foreground layer, enhancing the denoising effect on moving objects. 2. Debug the spatial parameters of the first three levels. Each level can separate foreground and background for independent debugging of spatial effects. Debug filter 7 as a mixing filter. Based on the current noise characteristics, adjust the filter 2 and 4 strengths and the mixing weights of filters 0~6 to suppress noise while minimizing loss of content-relevant areas. It is recommended to use larger weights for small window denoising but smaller filtering strengths.[¶](#typical-non-face-capture-recorder-application-scenarios-similar-to-previous-chip-tuning-the-focus-is-on-temporal-denoising-with-spatial-denoising-as-a-supplement-the-main-difference-compared-to-before-is-that-the-0th-level-of-luminance-denoising-and-chroma-denoising-supports-temporal-processing-and-can-be-coordinated-with-bnr-for-motionstill-decision-and-temporal-noise-reduction-debugging-1-it-is-recommended-to-enable-the-n0-reference-frame-set-math-mode-to-1-and-set-auto-math-to-around-128-appropriately-debug-the-bnr-temporal-parameters-tfs-and-tfr-in-coordination-with-the-overall-temporal-intensity-to-suppress-rain-like-noise-in-the-background-image-then-adjust-the-temporal-denoising-parameters-of-the-middle-two-levels-including-m-xtfs-m-xmath-m-xmabw-m-xmate-layers-0-and-1-of-n1-can-serve-as-the-foreground-and-background-layers-respectively-tune-m1math-of-the-background-layer-to-suppress-rain-like-noise-in-the-background-image-as-appropriate-then-tune-m1math-of-the-foreground-layer-to-control-some-foreground-motion-noise-tune-n1tfs-of-the-first-level-to-suppress-the-overall-noise-level-of-the-image-as-appropriate-balancing-the-temporal-denoising-effect-and-motion-smear-generally-tfs-of-the-foreground-layer-should-be-set-smaller-than-that-of-the-background-to-prevent-motion-object-smear-tune-m2math-and-n2tfs-of-the-second-level-to-control-the-overall-quietness-level-and-amplitude-of-the-noise-m2math-of-the-second-level-is-usually-set-smaller-than-m1math-of-the-first-level-to-prevent-smear-under-low-illumination-to-relieve-the-burden-on-math-the-mabw-parameter-can-be-appropriately-adjusted-under-extremely-low-illumination-the-mate-parameter-can-be-appropriately-adjusted-to-suppress-overall-image-noise-for-hierarchical-mode-the-foreground-layers-mabw-window-is-recommended-to-use-small-windows-04-if-using-adv-math-mode-the-foreground-layers-mabw-window-can-only-be-4-for-the-spatial-filter-types-of-the-middle-two-levels-it-is-recommended-to-use-filter-6-uniformly-however-the-first-level-should-increase-the-weight-of-filter-2-to-favor-denoising-capability-sacrificing-some-edge-preservation-ability-the-second-level-should-increase-the-weight-of-filter-4-to-favor-edge-preservation-removing-noise-in-non-edge-areas-for-the-hierarchical-mode-of-the-first-level-the-foreground-layers-n1tss-can-be-increased-to-mix-a-certain-proportion-of-spatial-filtering-results-into-the-foreground-layer-enhancing-the-denoising-effect-on-moving-objects-2-debug-the-spatial-parameters-of-the-first-three-levels-each-level-can-separate-foreground-and-background-for-independent-debugging-of-spatial-effects-debug-filter-7-as-a-mixing-filter-based-on-the-current-noise-characteristics-adjust-the-filter-2-and-4-strengths-and-the-mixing-weights-of-filters-06-to-suppress-noise-while-minimizing-loss-of-content-relevant-areas-it-is-recommended-to-use-larger-weights-for-small-window-denoising-but-smaller-filtering-strengths "锚链接")

1. The last level is a pure spatial filter. Still and motion areas can be debugged separately, with different spatial parameters configured. It is recommended to use filter 6 for enhancement processing, while using filter 7 to control the action strength and range of filter 6. Increase the weight of filter 4. By adjusting the filter 4 parameters appropriately, balance the improvement of graininess in flat areas and image sharpness. Finally, output through sth and sfn mixing.
2. After the luminance noise debugging is satisfactory, debug the chroma denoising N Rc interface.
3. Debug the chroma noise N0 parameters. Set the chroma motion/still decision threshold n Cmath to around 128, and adjust until the background chroma noise no longer flickers. It is recommended to set sfc to 31 to control motion area noise.
4. Debug the chroma noise N1 parameters. Different spatial filters can be used separately for the motion background and motion foreground. Use filter 4 or filter 6, with saturation, hue, and brightness tables for debugging and filter mixing to achieve spatial chroma denoising. Under low illumination, filter 5 (large window) can be used to control low-frequency noise.