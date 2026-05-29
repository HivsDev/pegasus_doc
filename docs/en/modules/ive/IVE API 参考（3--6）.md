---
title: IVE API 3–6
---

title: "Data Types and Data Structures"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVE API 参考/IVE API 参考（3--6）.md
--- # Data Types and Data Structures
<a name="ZH-CN_TOPIC_0000002471091210"></a>SVP-related data types and data structures are defined as follows: - [ot\_svp\_img\_type](#ZH-CN_TOPIC_0000002471091210): Defines the image types supported by 2D generalized images.
<a name="ZH-CN_TOPIC_0000002504091103"></a>- [ot\_svp\_img](#ZH-CN_TOPIC_0000002504091103): Defines 2D generalized image information.
<a name="ZH-CN_TOPIC_0000002471091254"></a>- [ot\_svp\_src\_img](#ZH-CN_TOPIC_0000002471091254): Defines the source image.
<a name="ZH-CN_TOPIC_0000002471091286"></a>- [ot\_svp\_dst\_img](#ZH-CN_TOPIC_0000002471091286): Defines the output image.
<a name="ZH-CN_TOPIC_0000002470931244"></a><a name="ZH-CN_TOPIC_0000002470931272"></a>- [OT\_SVP\_IMG\_ADDR\_NUM](#ZH-CN_TOPIC_0000002470931272): Defines the number of address channels. Fixed-point data types: - [ot\_svp\_data](#ZH-CN_TOPIC_0000002470931244): Defines 2D image information in bytes.
<a name="ZH-CN_TOPIC_0000002503971213"></a>- [ot\_svp\_src\_data](#ZH-CN_TOPIC_0000002503971213): Defines 2D source data information in bytes.
<a name="ZH-CN_TOPIC_0000002470931290"></a>- [ot\_svp\_dst\_data](#ZH-CN_TOPIC_0000002470931290): Defines 2D output data information in bytes.
<a name="ZH-CN_TOPIC_0000002503971231"></a>- [ot\_svp\_8bit](#ZH-CN_TOPIC_0000002503971231): Defines an 8-bit data union.
<a name="ZH-CN_TOPIC_0000002503971259"></a>- [ot\_svp\_point\_u16](#ZH-CN_TOPIC_0000002503971259): Defines a u16-bit point information structure.
<a name="ZH-CN_TOPIC_0000002504091193"></a>- [ot\_svp\_point\_s16](#ZH-CN_TOPIC_0000002504091193): Defines an s16-bit point information structure.
<a name="ZH-CN_TOPIC_0000002503971257"></a>- [ot\_svp\_point\_s25q7](#ZH-CN_TOPIC_0000002503971257): Defines a point information structure represented by s25q7.
<a name="ZH-CN_TOPIC_0000002504091195"></a>- [ot\_svp\_point\_u14q2](#ZH-CN_TOPIC_0000002504091195): Defines a point information structure represented by u14q2.
<a name="ZH-CN_TOPIC_0000002470931266"></a>- [ot\_svp\_rect\_u32](#ZH-CN_TOPIC_0000002470931266): Defines a rectangle information structure represented by u32.
<a name="ZH-CN_TOPIC_0000002470931214"></a>- [ot\_svp\_rect\_u16](#ZH-CN_TOPIC_0000002470931214): Defines a rectangle information structure represented by u16.
<a name="ZH-CN_TOPIC_0000002503971197"></a>- [ot\_svp\_rect\_s24q8](#ZH-CN_TOPIC_0000002503971197): Defines a rectangle information structure represented by s24q8.
<a name="ZH-CN_TOPIC_0000002471091250"></a><a name="ZH-CN_TOPIC_0000002503971221"></a>- [ot\_svp\_lut](#ZH-CN_TOPIC_0000002503971221): Defines a lookup table structure. IVE-related data types and data structures are defined as follows: - [ot\_ive\_handle](#ZH-CN_TOPIC_0000002471091250): Defines the IVE handle.
<a name="ZH-CN_TOPIC_0000002470931262"></a>- [OT\_IVE\_HIST\_NUM](#ZH-CN_TOPIC_0000002470931262): Defines the number of histogram bins.
- [OT\_IVE\_MAP\_NUM](#ZH-CN_TOPIC_0000002471091274): Defines the number of mapping lookup table entries.
- [OT\_IVE\_MAX\_RGN\_NUM](#ZH-CN_TOPIC_0000002471091214): Defines the maximum number of connected regions.
- [OT\_IVE\_ST\_MAX\_CORNER\_NUM](#ZH-CN_TOPIC_0000002503971193): Defines the maximum number of Shi-Tomasi-like corners.
- [OT\_IVE\_MASK\_NUM](#ZH-CN_TOPIC_0000002471091310): Mask array length.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_TWO](#ZH-CN_TOPIC_0000002503971159): Reserved field array length 2.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_THREE](#ZH-CN_TOPIC_0000002504091161): Reserved field array length 3.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_EIGHT](#ZH-CN_TOPIC_0000002470931298): Reserved field array length 8.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_TWELVE](#ZH-CN_TOPIC_0000002470931230): Reserved field array length 12.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_FOURTEEN](#ZH-CN_TOPIC_0000002470931216): Reserved field array length 14.
- [OT\_IVE\_ARR\_NUM\_THREE](#ZH-CN_TOPIC_0000002503971175): Array length 3.
- [OT\_IVE\_ARR\_NUM\_EIGHT](#ZH-CN_TOPIC_0000002503971255): Array length 8.
- [OT\_IVE\_DEV\_NAME\_LENGTH](#ZH-CN_TOPIC_0000002503971217): IVE device name length.
- [OT\_IVE\_DEV\_DEFAULT\_NODE\_NUM](#ZH-CN_TOPIC_0000002504091127): Default number of IVE nodes.
- [ot\_ive\_mod\_param](#ZH-CN_TOPIC_0000002504091147): IVE module related parameter definition.
<a name="ZH-CN_TOPIC_0000002504091141"></a>- [ot\_ive\_err\_code](#ZH-CN_TOPIC_0000002504091141): Defines error codes.
<a name="ZH-CN_TOPIC_0000002470931310"></a>- [ot\_ive\_dma\_mode](#ZH-CN_TOPIC_0000002470931310): Defines DMA operation mode.
<a name="ZH-CN_TOPIC_0000002504091157"></a>- [ot\_ive\_dma\_ctrl](#ZH-CN_TOPIC_0000002504091157): Defines DMA control information.
<a name="ZH-CN_TOPIC_0000002503971267"></a>- [ot\_ive\_filter\_ctrl](#ZH-CN_TOPIC_0000002503971267): Defines template filter control information.
<a name="ZH-CN_TOPIC_0000002470931222"></a>- [ot\_ive\_csc\_mode](#ZH-CN_TOPIC_0000002470931222): Defines color space conversion mode.
<a name="ZH-CN_TOPIC_0000002504091137"></a>- [ot\_ive\_csc\_ctrl](#ZH-CN_TOPIC_0000002504091137): Defines color space conversion control information.
<a name="ZH-CN_TOPIC_0000002471091222"></a>- [ot\_ive\_filter\_and\_csc\_ctrl](#ZH-CN_TOPIC_0000002471091222): Defines composite template filter plus color space conversion control information.
<a name="ZH-CN_TOPIC_0000002503971149"></a>- [ot\_ive\_sobel\_out\_ctrl](#ZH-CN_TOPIC_0000002503971149): Defines sobel output control information.
<a name="ZH-CN_TOPIC_0000002470931226"></a>- [ot\_ive\_sobel\_ctrl](#ZH-CN_TOPIC_0000002470931226): Defines sobel edge extraction control information.
<a name="ZH-CN_TOPIC_0000002471091234"></a>- [ot\_ive\_mag\_and\_ang\_out\_ctrl](#ZH-CN_TOPIC_0000002471091234): Defines the output format for canny edge magnitude and angle calculation.
<a name="ZH-CN_TOPIC_0000002470931264"></a>- [ot\_ive\_mag\_and\_ang\_ctrl](#ZH-CN_TOPIC_0000002470931264): Defines control information for canny edge magnitude and angle calculation.
<a name="ZH-CN_TOPIC_0000002504091109"></a>- [ot\_ive\_dilate\_ctrl](#ZH-CN_TOPIC_0000002504091109): Defines dilation control information.
<a name="ZH-CN_TOPIC_0000002470931312"></a>- [ot\_ive\_erode\_ctrl](#ZH-CN_TOPIC_0000002470931312): Defines erosion control information.
<a name="ZH-CN_TOPIC_0000002504091197"></a>- [ot\_ive\_threshold\_mode](#ZH-CN_TOPIC_0000002504091197): Defines image binarization output format.
<a name="ZH-CN_TOPIC_0000002504091163"></a>- [ot\_ive\_threshold\_ctrl](#ZH-CN_TOPIC_0000002504091163): Defines image binarization control information.
<a name="ZH-CN_TOPIC_0000002470931336"></a>- [ot\_ive\_sub\_mode](#ZH-CN_TOPIC_0000002470931336): Defines the output format for image subtraction.
<a name="ZH-CN_TOPIC_0000002471091290"></a>- [ot\_ive\_sub\_ctrl](#ZH-CN_TOPIC_0000002471091290): Defines control parameters for image subtraction.
<a name="ZH-CN_TOPIC_0000002504091081"></a>- [ot\_ive\_integ\_out\_ctrl](#ZH-CN_TOPIC_0000002504091081): Defines integral image output control parameters.
<a name="ZH-CN_TOPIC_0000002504091115"></a>- [ot\_ive\_integ\_ctrl](#ZH-CN_TOPIC_0000002504091115): Defines integral image calculation control parameters.
<a name="ZH-CN_TOPIC_0000002504091143"></a>- [ot\_ive\_threshold\_s16\_mode](#ZH-CN_TOPIC_0000002504091143): Defines thresholding mode for 16-bit signed images.
<a name="ZH-CN_TOPIC_0000002504091125"></a>- [ot\_ive\_threshold\_s16\_ctrl](#ZH-CN_TOPIC_0000002504091125): Defines thresholding control parameters for 16-bit signed images.
<a name="ZH-CN_TOPIC_0000002503971223"></a>- [ot\_ive\_threshold\_u16\_mode](#ZH-CN_TOPIC_0000002503971223): Defines thresholding mode for 16-bit unsigned images.
<a name="ZH-CN_TOPIC_0000002504091089"></a>- [ot\_ive\_threshold\_u16\_ctrl](#ZH-CN_TOPIC_0000002504091089): Defines thresholding control parameters for 16-bit unsigned images.
<a name="ZH-CN_TOPIC_0000002471091260"></a>- [ot\_ive\_16bit\_to\_8bit\_mode](#ZH-CN_TOPIC_0000002471091260): Defines conversion mode from 16-bit to 8-bit images.
<a name="ZH-CN_TOPIC_0000002470931316"></a>- [ot\_ive\_16bit\_to\_8bit\_ctrl](#ZH-CN_TOPIC_0000002470931316): Defines conversion control parameters from 16-bit to 8-bit images.
<a name="ZH-CN_TOPIC_0000002470931238"></a>- [ot\_ive\_order\_stats\_filter\_mode](#ZH-CN_TOPIC_0000002470931238): Defines order statistics filter mode.
<a name="ZH-CN_TOPIC_0000002471091240"></a>- [ot\_ive\_order\_stats\_filter\_ctrl](#ZH-CN_TOPIC_0000002471091240): Defines order statistics filter control parameters.
<a name="ZH-CN_TOPIC_0000002471091206"></a>- [ot\_ive\_map\_u8bit\_lut\_mem](#ZH-CN_TOPIC_0000002471091206): Defines the lookup table memory for Map U8C1->U8C1.
<a name="ZH-CN_TOPIC_0000002504091091"></a>- [ot\_ive\_map\_u16bit\_lut\_mem](#ZH-CN_TOPIC_0000002504091091): Defines the lookup table memory for Map U8C1->U16C1.
<a name="ZH-CN_TOPIC_0000002504091173"></a>- [ot\_ive\_map\_s16bit\_lut\_mem](#ZH-CN_TOPIC_0000002504091173): Defines the lookup table memory for Map U8C1->S16C1.
<a name="ZH-CN_TOPIC_0000002470931320"></a>- [ot\_ive\_map\_mode](#ZH-CN_TOPIC_0000002470931320): Defines Map mode.
<a name="ZH-CN_TOPIC_0000002471091224"></a>- [ot\_ive\_map\_ctrl](#ZH-CN_TOPIC_0000002471091224): Defines Map control parameters.
<a name="ZH-CN_TOPIC_0000002471091324"></a>- [ot\_ive\_equalize\_hist\_ctrl\_mem](#ZH-CN_TOPIC_0000002471091324): Defines histogram equalization auxiliary memory.
<a name="ZH-CN_TOPIC_0000002503971189"></a>- [ot\_ive\_equalize\_hist\_ctrl](#ZH-CN_TOPIC_0000002503971189): Defines histogram equalization control parameters.
<a name="ZH-CN_TOPIC_0000002503971153"></a>- [ot\_ive\_add\_ctrl](#ZH-CN_TOPIC_0000002503971153): Defines weighted addition control parameters for two images.
<a name="ZH-CN_TOPIC_0000002503971173"></a>- [ot\_ive\_ncc\_dst\_mem](#ZH-CN_TOPIC_0000002503971173): Defines NCC output memory information.
<a name="ZH-CN_TOPIC_0000002471091252"></a>- [ot\_ive\_rgn](#ZH-CN_TOPIC_0000002471091252): Defines connected region information.
<a name="ZH-CN_TOPIC_0000002503971207"></a>- [ot\_ive\_ccblob](#ZH-CN_TOPIC_0000002503971207): Defines the output information for connected component labeling.
<a name="ZH-CN_TOPIC_0000002470931332"></a>- [ot\_ive\_ccl\_mode](#ZH-CN_TOPIC_0000002470931332): Defines connected component labeling mode.
<a name="ZH-CN_TOPIC_0000002471091318"></a>- [ot\_ive\_ccl\_ctrl](#ZH-CN_TOPIC_0000002471091318): Defines connected component labeling control parameters.
<a name="ZH-CN_TOPIC_0000002471091236"></a>- [ot\_ive\_gmm\_ctrl](#ZH-CN_TOPIC_0000002471091236): Defines control parameters for GMM background modeling.
<a name="ZH-CN_TOPIC_0000002471091300"></a>- [ot\_ive\_gmm2\_sns\_factor\_mode](#ZH-CN_TOPIC_0000002471091300): Defines sensitivity factor mode.
<a name="ZH-CN_TOPIC_0000002503971203"></a>- [ot\_ive\_gmm2\_life\_update\_factor\_mode](#ZH-CN_TOPIC_0000002503971203): Defines model lifetime parameter update mode.
<a name="ZH-CN_TOPIC_0000002504091119"></a>- [ot\_ive\_gmm2\_ctrl](#ZH-CN_TOPIC_0000002504091119): Defines control parameters for GMM2 background modeling.
<a name="ZH-CN_TOPIC_0000002504091083"></a>- [ot\_ive\_canny\_stack\_size](#ZH-CN_TOPIC_0000002504091083): Defines the strong edge point stack size structure for the first half of Canny edge calculation.
<a name="ZH-CN_TOPIC_0000002503971183"></a>- [ot\_ive\_canny\_hys\_edge\_ctrl](#ZH-CN_TOPIC_0000002503971183): Defines control parameters for the first half of Canny edge calculation task.
<a name="ZH-CN_TOPIC_0000002470931250"></a>- [ot\_ive\_lbp\_compare\_mode](#ZH-CN_TOPIC_0000002470931250): Defines LBP texture calculation control parameters.
<a name="ZH-CN_TOPIC_0000002471091226"></a>- [ot\_ive\_lbp\_ctrl](#ZH-CN_TOPIC_0000002471091226): Defines LBP texture calculation control parameters.
<a name="ZH-CN_TOPIC_0000002503971179"></a>- [ot\_ive\_norm\_grad\_out\_ctrl](#ZH-CN_TOPIC_0000002503971179): Defines the output control enumeration type for normalized gradient information calculation.
<a name="ZH-CN_TOPIC_0000002470931288"></a>- [ot\_ive\_norm\_grad\_ctrl](#ZH-CN_TOPIC_0000002470931288): Defines control parameters for normalized gradient information calculation.
<a name="ZH-CN_TOPIC_0000002504091077"></a>- [ot\_ive\_lk\_optical\_flow\_pyr\_out\_mode](#ZH-CN_TOPIC_0000002504091077): Defines the output mode for pyramidal LK optical flow calculation.
<a name="ZH-CN_TOPIC_0000002503971181"></a>- [ot\_ive\_lk\_optical\_flow\_pyr\_ctrl](#ZH-CN_TOPIC_0000002503971181): Defines control parameters for pyramidal LK optical flow calculation.
<a name="ZH-CN_TOPIC_0000002504091183"></a>- [ot\_ive\_st\_max\_eig\_val](#ZH-CN_TOPIC_0000002504091183): Defines the maximum corner response value structure for Shi-Tomasi-like corner calculation.
<a name="ZH-CN_TOPIC_0000002504091117"></a>- [ot\_ive\_st\_cand\_corner\_ctrl](#ZH-CN_TOPIC_0000002504091117): Defines control parameters for Shi-Tomasi-like candidate corner calculation.
<a name="ZH-CN_TOPIC_0000002503971265"></a>- [ot\_ive\_st\_corner\_info](#ZH-CN_TOPIC_0000002503971265): Defines the corner information structure output from Shi-Tomasi-like corner calculation.
<a name="ZH-CN_TOPIC_0000002471091220"></a>- [ot\_ive\_st\_corner\_ctrl](#ZH-CN_TOPIC_0000002471091220): Defines control parameters for Shi-Tomasi-like corner filtering.
<a name="ZH-CN_TOPIC_0000002470931274"></a>- [ot\_ive\_sad\_mode](#ZH-CN_TOPIC_0000002470931274): Defines SAD calculation mode.
<a name="ZH-CN_TOPIC_0000002471091278"></a>- [ot\_ive\_sad\_out\_ctrl](#ZH-CN_TOPIC_0000002471091278): Defines SAD output control mode.
<a name="ZH-CN_TOPIC_0000002471091212"></a>- [ot\_ive\_sad\_ctrl](#ZH-CN_TOPIC_0000002471091212): Defines SAD control parameters.
<a name="ZH-CN_TOPIC_0000002503971219"></a>- [ot\_ive\_resize\_mode](#ZH-CN_TOPIC_0000002503971219): Defines Resize mode.
<a name="ZH-CN_TOPIC_0000002471091258"></a>- [ot\_ive\_resize\_ctrl](#ZH-CN_TOPIC_0000002471091258): Defines Resize control parameters.
<a name="ZH-CN_TOPIC_0000002503971161"></a>- [ot\_ive\_grad\_fg\_mode](#ZH-CN_TOPIC_0000002503971161): Defines gradient foreground calculation mode.
<a name="ZH-CN_TOPIC_0000002504091111"></a>- [ot\_ive\_grad\_fg\_ctrl](#ZH-CN_TOPIC_0000002504091111): Defines gradient foreground calculation control parameters.
<a name="ZH-CN_TOPIC_0000002503971261"></a>- [ot\_ive\_cand\_bg\_pixel](#ZH-CN_TOPIC_0000002503971261): Defines candidate background model data.
<a name="ZH-CN_TOPIC_0000002503971171"></a>- [ot\_ive\_wrok\_bg\_pixel](#ZH-CN_TOPIC_0000002503971171): Defines working background model data.
<a name="ZH-CN_TOPIC_0000002471091208"></a>- [ot\_ive\_bg\_life](#ZH-CN_TOPIC_0000002471091208): Defines background lifetime data.
<a name="ZH-CN_TOPIC_0000002503971177"></a>- [ot\_ive\_bg\_model\_pixel](#ZH-CN_TOPIC_0000002503971177): Defines background model data.
<a name="ZH-CN_TOPIC_0000002503971239"></a>- [ot\_ive\_fg\_status\_data](#ZH-CN_TOPIC_0000002503971239): Defines foreground status data.
<a name="ZH-CN_TOPIC_0000002503971253"></a>- [ot\_ive\_bg\_status\_data](#ZH-CN_TOPIC_0000002503971253): Defines background status data.
<a name="ZH-CN_TOPIC_0000002503971249"></a>- [ot\_ive\_match\_bg\_model\_ctrl](#ZH-CN_TOPIC_0000002503971249): Defines background matching control parameters.
<a name="ZH-CN_TOPIC_0000002471091248"></a>- [ot\_ive\_update\_bg\_model\_ctrl](#ZH-CN_TOPIC_0000002471091248): Defines background update control parameters.
<a name="ZH-CN_TOPIC_0000002504091185"></a>- [ot\_ive\_ann\_mlp\_accurate](#ZH-CN_TOPIC_0000002504091185): Defines ann\_mlp input feature vector type.
<a name="ZH-CN_TOPIC_0000002503971151"></a>- [ot\_ive\_ann\_mlp\_actv\_func](#ZH-CN_TOPIC_0000002503971151): Defines ann\_mlp activation function enumeration type.
<a name="ZH-CN_TOPIC_0000002503971233"></a>- [ot\_ive\_ann\_mlp\_model](#ZH-CN_TOPIC_0000002503971233): Defines ann\_mlp model data structure.
<a name="ZH-CN_TOPIC_0000002471091314"></a>- [ot\_ive\_svm\_type](#ZH-CN_TOPIC_0000002471091314): Defines SVM type.
<a name="ZH-CN_TOPIC_0000002471091268"></a>- [ot\_ive\_svm\_kernel\_type](#ZH-CN_TOPIC_0000002471091268): Defines SVM kernel function type.
<a name="ZH-CN_TOPIC_0000002470931338"></a>- [ot\_ive\_svm\_model](#ZH-CN_TOPIC_0000002470931338): Defines SVM model data structure.
<a name="ZH-CN_TOPIC_0000002470931254"></a>- [ot\_ive\_cnn\_actv\_func](#ZH-CN_TOPIC_0000002470931254): Defines CNN activation function enumeration type.
<a name="ZH-CN_TOPIC_0000002471091230"></a>- [ot\_ive\_cnn\_pooling](#ZH-CN_TOPIC_0000002471091230): Defines CNN pooling operation enumeration type.
<a name="ZH-CN_TOPIC_0000002471091306"></a>- [ot\_ive\_cnn\_conv\_pooling](#ZH-CN_TOPIC_0000002471091306): Defines CNN single-layer Conv-Re LU-Pooling operation package parameter structure.
<a name="ZH-CN_TOPIC_0000002470931296"></a>- [ot\_ive\_cnn\_fc\_info](#ZH-CN_TOPIC_0000002470931296): Defines CNN fully connected network parameter structure.
<a name="ZH-CN_TOPIC_0000002504091131"></a>- [ot\_ive\_cnn\_model](#ZH-CN_TOPIC_0000002504091131): Defines CNN model parameter structure.
<a name="ZH-CN_TOPIC_0000002471091238"></a>- [ot\_ive\_cnn\_ctrl](#ZH-CN_TOPIC_0000002471091238): Defines control parameters for CNN prediction task.
<a name="ZH-CN_TOPIC_0000002503971157"></a>- [ot\_ive\_cnn\_result](#ZH-CN_TOPIC_0000002503971157): Defines CNN single sample prediction result structure.
<a name="ZH-CN_TOPIC_0000002470931326"></a>- [ot\_ive\_persp\_trans\_point\_pair](#ZH-CN_TOPIC_0000002470931326): Defines perspective transformation point pair structure.
<a name="ZH-CN_TOPIC_0000002471091242"></a>- [ot\_ive\_persp\_trans\_alg\_mode](#ZH-CN_TOPIC_0000002471091242): Defines perspective transformation algorithm mode enumeration.
<a name="ZH-CN_TOPIC_0000002470931228"></a>- [ot\_ive\_persp\_trans\_csc\_mode](#ZH-CN_TOPIC_0000002470931228): Defines perspective transformation color space conversion mode.
<a name="ZH-CN_TOPIC_0000002504091191"></a>- [ot\_ive\_kcf\_core\_id](#ZH-CN_TOPIC_0000002504091191): Defines KCF kernel ID.
<a name="ZH-CN_TOPIC_0000002471091262"></a>- [ot\_ive\_persp\_trans\_ctrl](#ZH-CN_TOPIC_0000002471091262): Defines perspective transformation control parameters.
<a name="ZH-CN_TOPIC_0000002503971155"></a>- [ot\_ive\_roi\_info](#ZH-CN_TOPIC_0000002503971155): Defines region of interest information parameters.
<a name="ZH-CN_TOPIC_0000002471091264"></a>- [ot\_ive\_kcf\_proc\_ctrl](#ZH-CN_TOPIC_0000002471091264): Defines tracking processing control parameters.
<a name="ZH-CN_TOPIC_0000002504091189"></a>- [ot\_ive\_list\_head](#ZH-CN_TOPIC_0000002504091189): Defines linked list head structure parameters.
<a name="ZH-CN_TOPIC_0000002471091292"></a>- [ot\_ive\_kcf\_obj](#ZH-CN_TOPIC_0000002471091292): Defines target information structure parameters.
<a name="ZH-CN_TOPIC_0000002470931324"></a>- [ot\_ive\_kcf\_obj\_node](#ZH-CN_TOPIC_0000002470931324): Defines target linked list node parameters.
<a name="ZH-CN_TOPIC_0000002504091113"></a>- [ot\_ive\_kcf\_list\_state](#ZH-CN_TOPIC_0000002504091113): Defines target linked list state enumeration type.
<a name="ZH-CN_TOPIC_0000002470931236"></a>- [ot\_ive\_kcf\_obj\_list](#ZH-CN_TOPIC_0000002470931236): Defines target linked list structure parameters.
<a name="ZH-CN_TOPIC_0000002504091101"></a>- [ot\_ive\_kcf\_bbox](#ZH-CN_TOPIC_0000002504091101): Defines target region information parameters.
<a name="ZH-CN_TOPIC_0000002470931278"></a>- [ot\_ive\_kcf\_bbox\_ctrl](#ZH-CN_TOPIC_0000002470931278): Defines target region information control parameters.
<a name="ZH-CN_TOPIC_0000002504091097"></a>- [ot\_ive\_hog\_mode](#ZH-CN_TOPIC_0000002504091097): Defines HOG (Histogram of Oriented Gradient) feature storage mode enumeration type.
<a name="ZH-CN_TOPIC_0000002470931248"></a>- [ot\_ive\_hog\_ctrl](#ZH-CN_TOPIC_0000002470931248): Defines HOG (Histogram of Oriented Gradient) feature calculation control parameters. ## SVP-Related Data Types and Data Structures ### ot\_svp\_img\_type 【Description】 Defines the image types supported by 2D generalized images. 【Definition】 `/* Img type */
typedef enum { OT_SVP_IMG_TYPE_U8C1 = 0x0, OT_SVP_IMG_TYPE_S8C1 = 0x1, OT_SVP_IMG_TYPE_YUV420SP = 0x2, /* YUV420 Semi Planar */ OT_SVP_IMG_TYPE_YUV422SP = 0x3, /* YUV422 Semi Planar */ OT_SVP_IMG_TYPE_YUV420P = 0x4, /* YUV420 Planar */ OT_SVP_IMG_TYPE_YUV422P = 0x5, /* YUV422 planar */ OT_SVP_IMG_TYPE_S8C2_PACKAGE = 0x6, OT_SVP_IMG_TYPE_S8C2_PLANAR = 0x7, OT_SVP_IMG_TYPE_S16C1 = 0x8, OT_SVP_IMG_TYPE_U16C1 = 0x9, OT_SVP_IMG_TYPE_U8C3_PACKAGE = 0xa, OT_SVP_IMG_TYPE_U8C3_PLANAR = 0xb, OT_SVP_IMG_TYPE_S32C1 = 0xc, OT_SVP_IMG_TYPE_U32C1 = 0xd, OT_SVP_IMG_TYPE_S64C1 = 0xe, OT_SVP_IMG_TYPE_U64C1 = 0xf, OT_SVP_IMG_TYPE_BUTT } ot_svp_img_type;` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_SVP\_IMG\_TYPE\_U8C1 | A single-channel image where each pixel is represented by 1 8-bit unsigned data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_S8C1 | A single-channel image where each pixel is represented by 1 8-bit signed data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_YUV420SP | YUV420 Semiplanar format image.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_YUV420SP. |
| OT\_SVP\_IMG\_TYPE\_YUV422SP | YUV422 Semiplanar format image.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_YUV422SP. |
| OT\_SVP\_IMG\_TYPE\_YUV420P | YUV420 Planar format image. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_YUV420P. |
| OT\_SVP\_IMG\_TYPE\_YUV422P | YUV422 Planar format image. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_YUV422P. |
| OT\_SVP\_IMG\_TYPE\_S8C2\_PACKAGE | A 2-channel image where each pixel is represented by 2 8-bit signed data stored in package format.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_S8C2\_PACKAGE. |
| OT\_SVP\_IMG\_TYPE\_S8C2\_PLANAR | A 2-channel image where each pixel is represented by 2 8-bit signed data stored in planar format.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_S8C2\_PLANAR. |
| OT\_SVP\_IMG\_TYPE\_S16C1 | A single-channel image where each pixel is represented by 1 16-bit signed data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_U16C1 | A single-channel image where each pixel is represented by 1 16-bit unsigned data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_U8C3\_PACKAGE | A 3-channel image where each pixel is represented by 3 8-bit unsigned data stored in Package format.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C3\_PACKAGE. |
| OT\_SVP\_IMG\_TYPE\_U8C3\_PLANAR | A 3-channel image where each pixel is represented by 3 8-bit unsigned data stored in planar format.  See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C3\_PLANAR. |
| OT\_SVP\_IMG\_TYPE\_S32C1 | A single-channel image where each pixel is represented by 1 32-bit signed data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_U32C1 | A single-channel image where each pixel is represented by 1 32-bit unsigned data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_S64C1 | A single-channel image where each pixel is represented by 1 64-bit signed data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |
| OT\_SVP\_IMG\_TYPE\_U64C1 | A single-channel image where each pixel is represented by 1 64-bit unsigned data. See the ot\_svp\_img image diagram for OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1. |

【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_src\_img](#ot_svp_src_img)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_img 【Description】 Defines 2D generalized image information. 【Definition】 `typedef struct { td_u64 phys_addr[OT_SVP_IMG_ADDR_NUM]; /* RW;The physical address of the image */ td_u64 virt_addr[OT_SVP_IMG_ADDR_NUM]; /* RW;The virtual address of the image */ td_u32 stride[OT_SVP_IMG_STRIDE_NUM]; /* RW;The stride of the image */ td_u32 width; /* RW;The width of the image */ td_u32 height; /* RW;The height of the image */ ot_svp_img_type type; /* RW;The type of the image */
} ot_svp_img;` 【Members】

| Member Name | Description |
| --- | --- |
| phys\_addr[[OT\_SVP\_IMG\_ADDR\_NUM](#ZH-CN_TOPIC_0000002470931272)] | Physical address array of the generalized image. |
| virt\_addr[OT\_SVP\_IMG\_ADDR\_NUM] | Virtual address array of the generalized image. |
| stride[OT\_SVP\_IMG\_STRIDE\_NUM] | Stride of the generalized image. |
| width | Width of the generalized image. |
| height | Height of the generalized image. |
| type | Type of the generalized image. |

【Notes】 For image diagrams under each type, refer to the ot\_svp\_img image diagrams for types OT\_SVP\_IMG\_TYPE\_U8C1 \ OT\_SVP\_IMG\_TYPE\_S8C1 \ OT\_SVP\_IMG\_TYPE\_S16C1 \ OT\_SVP\_IMG\_TYPE\_U16C1 \ OT\_SVP\_IMG\_TYPE\_S32C1 \ OT\_SVP\_IMG\_TYPE\_U32C1 \ OT\_SVP\_IMG\_TYPE\_S64C1 \ OT\_SVP\_IMG\_TYPE\_U64C1 through OT\_SVP\_IMG\_TYPE\_U8C3\_PLANAR. 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_src\_img](#ot_svp_src_img)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_src\_img 【Description】 Defines the source image. 【Definition】 `typedef ot_svp_img ot_svp_src_img;` 【Members】 None 【Notes】 None 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_dst\_img 【Description】 Defines the output image. 【Definition】 `typedef ot_svp_img ot_svp_dst_img;` 【Members】 None 【Notes】 None 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_src\_img](#ot_svp_src_img) ### OT\_SVP\_IMG\_ADDR\_NUM 【Description】 Defines the number of address channels. 【Definition】 ```

# define OT\_SVP\_IMAE\_ADDR\_NUM 3[¶](#define-ot_svp_imae_addr_num-3 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_SVP\_IMG\_STRIDE\_NUM<a name="ZH-CN_TOPIC_0000002470931232"></a> 【Description】 Defines the stride array length. 【Definition】`

# define OT\_SVP\_IMG\_STRIDE\_NUM 3[¶](#define-ot_svp_img_stride_num-3 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ## Fixed-Point Data Types<a name="ZH-CN_TOPIC_0000002471091272"></a> 【Description】 Defines fixed-point data types. 【Definition】`
typedef unsigned char td\_u0q8;
typedef unsigned char td\_u1q7;
typedef unsigned char td\_u5q3;
typedef unsigned char td\_u3q5; typedef unsigned short td\_u0q16;
typedef unsigned short td\_u4q12;
typedef unsigned short td\_u6q10;
typedef unsigned short td\_u8q8;
typedef unsigned short td\_u9q7;
typedef unsigned short td\_u12q4;
typedef unsigned short td\_u14q2;
typedef unsigned short td\_u5q11;
typedef unsigned short td\_u1q15;
typedef unsigned short td\_u2q14;
typedef td\_u6q10 td\_ufp16;
typedef short td\_s9q7;
typedef short td\_s14q2;
typedef short td\_s1q15; typedef unsigned int td\_u22q10;
typedef unsigned int td\_u25q7;
typedef unsigned int td\_u21q11;
typedef unsigned int td\_u14q18;
typedef unsigned int td\_u8q24;
typedef unsigned int td\_u4q28; typedef int td\_s25q7;
typedef int td\_s16q16;
typedef int td\_s14q18;
typedef int td\_s20q12;
typedef int td\_s24q8; typedef unsigned short td\_u8q4f4;
``` 【Members】

| Member Name | Description |
| --- | --- |
| td\_u0q8 | 0 bits for integer part, 8 bits for fractional part. Represented as UQ0.8 in the documentation. |
| td\_u1q7 | Upper 1 unsigned bit for integer part, lower 7 bits for fractional part. Represented as UQ1.7 in the documentation. |
| td\_u5q3 | Upper 5 unsigned bits for integer part, lower 3 bits for fractional part. Represented as UQ5.3 in the documentation. |
| td\_u3q5 | Upper 3 unsigned bits for integer part, lower 5 bits for fractional part. Represented as UQ3.5 in the documentation. |
| td\_u0q16 | 0 bits for integer part, 16 bits for fractional part. Represented as UQ0.16 in the documentation. |
| td\_u4q12 | Upper 4 unsigned bits for integer part, lower 12 bits for fractional part. Represented as UQ4.12 in the documentation. |
| td\_u6q10 | Upper 6 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ6.10 in the documentation. |
| td\_u8q8 | Upper 8 unsigned bits for integer part, lower 8 bits for fractional part. Represented as UQ8.8 in the documentation. |
| td\_u9q7 | Upper 9 unsigned bits for integer part, lower 7 bits for fractional part. Represented as UQ9.7 in the documentation. |
| td\_u12q4 | Upper 12 unsigned bits for integer part, lower 4 bits for fractional part. Represented as UQ12.4 in the documentation. |
| td\_u14q2 | Upper 14 unsigned bits for integer part, lower 2 bits for fractional part. Represented as UQ14.2 in the documentation. |
| td\_u5q11 | Upper 5 unsigned bits for integer part, lower 11 bits for fractional part. Represented as UQ5.11 in the documentation. |
| td\_u1q15 | Upper 1 unsigned bit for integer part, lower 15 bits for fractional part. Represented as UQ1.15 in the documentation. |
| td\_u2q14 | Upper 2 unsigned bits for integer part, lower 14 bits for fractional part. Represented as UQ2.14 in the documentation. |
| td\_ufp16 | Upper 6 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ6.10 in the documentation. |
| td\_s9q7 | Upper 9 signed bits for integer part, lower 7 bits for fractional part. Represented as SQ9.7 in the documentation. |
| td\_s14q2 | Upper 14 signed bits for integer part, lower 2 bits for fractional part. Represented as SQ14.2 in the documentation. |
| td\_s1q15 | Upper 1 signed bit for integer part, lower 15 bits for fractional part. Represented as SQ1.15 in the documentation. |
| td\_u22q10 | Upper 22 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ22.10 in the documentation. |
| td\_u25q7 | Upper 25 unsigned bits for integer part, lower 7 bits for fractional part. Represented as UQ25.7 in the documentation. |
| td\_u21q11 | Upper 21 unsigned bits for integer part, lower 11 bits for fractional part. Represented as UQ21.11 in the documentation. |
| td\_u14q18 | Upper 14 unsigned bits for integer part, lower 18 bits for fractional part. Represented as UQ14.18 in the documentation. |
| td\_u8q24 | Upper 8 unsigned bits for integer part, lower 24 bits for fractional part. Represented as UQ8.24 in the documentation. |
| td\_u4q28 | Upper 4 unsigned bits for integer part, lower 28 bits for fractional part. Represented as UQ4.28 in the documentation. | td\_s25q7 | Upper 25 signed bits for integer part, lower 7 bits for fractional part. Represented as SQ25.7 in the documentation. |
| td\_s16q16 | Upper 16 signed bits for integer part, lower 16 bits for fractional part. Represented as SQ16.16 in the documentation. |
| td\_s14q18 | Upper 14 signed bits for integer part, lower 18 bits for fractional part. Represented as SQ14.18 in the documentation. |
| td\_s20q12 | Upper 20 signed bits for integer part, lower 12 bits for fractional part. Represented as SQ20.12 in the documentation. |
| td\_s24q8 | Upper 24 signed bits for integer part, lower 8 bits for fractional part. Represented as SQ24.8 in the documentation. |
| td\_u8q4f4 | Upper 8 unsigned bits for integer part, middle 4 bits for fractional part, lower 4 bits for flags. Represented as UQF8.4.4 in the documentation. |

【Notes】 td\_uxqyfz\td\_sxqy: - The number x after u indicates x unsigned bits for the integer part.
- The number x after s indicates x signed bits for the integer part.
- The number y after q indicates y bits for the fractional part.
- The number z after f indicates z bits for the flag bits.
- From left to right, high bits to low bits. 【Related Data Types and AP Is】 None. ### ot\_svp\_data 【Description】 Defines 2D data information in bytes. 【Definition】 `typedef struct { td_u64 phys_addr; /* RW;The physical address of the data */ td_u64 virt_addr; /* RW;The virtaul address of the data */ td_u32 stride; /* RW;The stride of 2D data by byte */ td_u32 width; /* RW;The width of 2D data by byte */ td_u32 height; /* RW;The height of 2D data by byte */ td_u32 reserved;
} ot_svp_data;` 【Members】

| Member Name | Description |
| --- | --- |
| phys\_addr | Image physical address. |
| virt\_addr | Image virtual address. |
| stride | Image stride. |
| height | Image height. |
| width | Image width. |
| reserved | Reserved bit. |

【Notes】 Represents 2D data in bytes; can be converted to/from [ot\_svp\_img](#ZH-CN_TOPIC_0000002504091103). 【Related Data Types and AP Is】 None. ### ot\_svp\_src\_data 【Description】 Defines 2D source data information in bytes. 【Definition】 `typedef ot_svp_data ot_svp_src_data;` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_dst\_data](#ot_svp_dst_data) ### ot\_svp\_dst\_data 【Description】 Defines 2D output data information in bytes. 【Definition】 `typedef ot_svp_data ot_svp_dst_data;` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_src\_img](#ot_svp_src_img) ### ot\_svp\_8bit 【Description】 Defines an 8-bit data union. 【Definition】 `typedef union { td_s8 s8_val; td_u8 u8_val;
} ot_svp_8bit;` 【Members】 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_u16 【Description】 Defines a point information structure represented by u16. 【Definition】 `typedef struct { td_u16 x; /* RW;The X coordinate of the point */ td_u16 y; /* RW;The Y coordinate of the point */
} ot_svp_point_u16;` 【Members】

| Member Name | Description |
| --- | --- |
| x | X coordinate of the point. |
| y | Y coordinate of the point. |

【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_s16 【Description】 Defines a point information structure represented by s16. 【Definition】 `typedef struct { td_s16 x; /* RW;The X coordinate of the point */ td_s16 y; /* RW;The Y coordinate of the point */
} ot_svp_point_s16;` 【Members】

| Member Name | Description |
| --- | --- |
| x | X coordinate of the point. |
| y | Y coordinate of the point. |

【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_s25q7 【Description】 Defines a point information structure represented by s25q7. 【Definition】 `typedef struct { td_s25q7 x; /* RW;The X coordinate of the point */ td_s25q7 y; /* RW;The Y coordinate of the point */
} ot_svp_point_s25q7;` 【Members】

| Member Name | Description |
| --- | --- |
| x | X coordinate of the point, expressed in SQ25.7. |
| y | Y coordinate of the point, expressed in SQ25.7. |

【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_u14q2 【Description】 Defines a point information structure represented by u14q2. 【Definition】 `typedef struct { td_u14q2 x; td_u14q2 y;
} ot_svp_point_u14q2;` 【Members】

| Member Name | Description |
| --- | --- |
| x | X coordinate of the point. |
| y | Y coordinate of the point. |

【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_rect\_u32 【Description】 Defines a rectangle information structure represented by u32. 【Definition】 `typedef struct { td_u32 x; /* RW;The location of X axis of the rectangle */ td_u32 y; /* RW;The location of Y axis of the rectangle */ td_u32 width; /* RW;The width of the rectangle */ td_u32 height; /* RW;The height of the rectangle */
} ot_svp_rect_u32;` 【Members】

| Member Name | Description |
| --- | --- |
| x | X coordinate of the point of the rectangle closest to the origin. |
| y | Y coordinate of the point of the rectangle closest to the origin. |
| width | Width of the rectangle. |
| height | Height of the rectangle. |

【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_rect\_u16 【Description】 Defines a rectangle information structure represented by u16. 【Definition】 `typedef struct { td_u16 x; /* RW;The location of X axis of the rectangle */ td_u16 y; /* RW;The location of Y axis of the rectangle */ td_u16 width; /* RW;The width of the rectangle */ td_u16 height; /* RW;The height of the rectangle */
} ot_svp_rect_u16;` 【Members】 【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_rect\_s24q8 【Description】 Defines a rectangle information structure represented by s24q8. 【Definition】 `typedef struct { td_s24q8 x; td_s24q8 y; td_u32 width; td_u32 height;
} ot_svp_rect_s24q8;` 【Members】 【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_lut 【Description】 Defines a lookup table structure. 【Definition】 `typedef struct { ot_svp_mem_info table; td_u16 elem_num; /* RW;LUT's elements number */ td_u8 table_in_precision; td_u8 table_out_norm; td_s32 table_in_lower; /* RW;LUT's original input lower limit */ td_s32 table_in_upper; /* RW;LUT's original input upper limit */
} ot_svp_lut;` 【Members】

| Member Name | Description |
| --- | --- |
| table | Data memory block information after the lookup table is established. |
| elem\_num | Number of elements in the lookup table. |
| table\_in\_precision | Lower limit of the value range for establishing the lookup table. |
| table\_out\_norm | Upper limit of the value range for establishing the lookup table. |
| table\_in\_lower | Precision for establishing the lookup table. (table\_in\_upper - table\_in\_lower)/(1<< table\_in\_precision) indicates the interval for establishing the lookup table. |
| table\_in\_upper | Number of bits to shift or divisor to use when normalizing the original data for establishing the lookup table. |

【Notes】 None 【Related Data Types and Structures】 None ## IVE-Related Data Types and Data Structures ### ot\_ive\_handle 【Description】 Defines the IVE handle. 【Definition】 `typedef td_s32 ot_ive_handle;` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_HIST\_NUM 【Description】 Defines the number of histogram bins. 【Definition】 ```

# define OT\_IVE\_HIST\_NUM 256[¶](#define-ot_ive_hist_num-256 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MAP\_NUM<a name="ZH-CN_TOPIC_0000002471091274"></a> 【Description】 Defines the number of mapping lookup table entries. 【Definition】`

# define OT\_IVE\_MAP\_NUM 256[¶](#define-ot_ive_map_num-256 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MAX\_RGN\_NUM<a name="ZH-CN_TOPIC_0000002471091214"></a> 【Description】 Defines the maximum number of connected regions. 【Definition】`

# define OT\_IVE\_MAX\_RGN\_NUM 254[¶](#define-ot_ive_max_rgn_num-254 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_ST\_MAX\_CORNER\_NUM<a name="ZH-CN_TOPIC_0000002503971193"></a> 【Description】 Defines the maximum number of Shi-Tomasi-like corners. 【Definition】`

# define OT\_IVE\_ST\_MAX\_CORNER\_NUM 500[¶](#define-ot_ive_st_max_corner_num-500 "锚链接")

`【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MASK\_NUM<a name="ZH-CN_TOPIC_0000002471091310"></a> 【Description】 Length of the mask array. 【Definition】`

# define OT\_IVE\_MASK\_NUM 25[¶](#define-ot_ive_mask_num-25 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_TWO<a name="ZH-CN_TOPIC_0000002503971159"></a> 【Description】 Reserved field array length 2. 【Definition】`

# define OT\_IVE\_ARR\_RESERVED\_NUM\_TWO 2[¶](#define-ot_ive_arr_reserved_num_two-2 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_THREE<a name="ZH-CN_TOPIC_0000002504091161"></a> 【Description】 Reserved field array length 3. 【Definition】`

# define OT\_IVE\_ARR\_RESERVED\_NUM\_THREE 3[¶](#define-ot_ive_arr_reserved_num_three-3 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_EIGHT<a name="ZH-CN_TOPIC_0000002470931298"></a> 【Description】 Reserved field array length 8. 【Definition】`

# define OT\_IVE\_ARR\_RESERVED\_NUM\_EIGHT 8[¶](#define-ot_ive_arr_reserved_num_eight-8 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_TWELVE<a name="ZH-CN_TOPIC_0000002470931230"></a> 【Description】 Reserved field array length 12. 【Definition】`

# define OT\_IVE\_ARR\_RESERVED\_NUM\_TWELVE 12[¶](#define-ot_ive_arr_reserved_num_twelve-12 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_FOURTEEN<a name="ZH-CN_TOPIC_0000002470931216"></a> 【Description】 Reserved field array length 14. 【Definition】`

# define OT\_IVE\_ARR\_RESERVED\_NUM\_FOURTEEN 14[¶](#define-ot_ive_arr_reserved_num_fourteen-14 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_NUM\_THREE<a name="ZH-CN_TOPIC_0000002503971175"></a> 【Description】 Array length 3. 【Definition】`

# define OT\_IVE\_ARR\_NUM\_THREE 3[¶](#define-ot_ive_arr_num_three-3 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_NUM\_EIGHT<a name="ZH-CN_TOPIC_0000002503971255"></a> 【Description】 Array length 8. 【Definition】`

# define OT\_IVE\_ARR\_NUM\_EIGHT 8[¶](#define-ot_ive_arr_num_eight-8 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_DEV\_NAME\_LENGTH<a name="ZH-CN_TOPIC_0000002503971217"></a> 【Description】 IVE device name length. 【Definition】`

# define OT\_IVE\_DEV\_NAME\_LENGTH 10[¶](#define-ot_ive_dev_name_length-10 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_DEV\_DEFAULT\_NODE\_NUM<a name="ZH-CN_TOPIC_0000002504091127"></a> 【Description】 Default number of IVE nodes. 【Definition】`

# define OT\_IVE\_DEFAULT\_NODE\_NUM 512[¶](#define-ot_ive_default_node_num-512 "锚链接")

`【Members】 None 【Related Data Types and AP Is】 None ### ot\_ive\_mod\_param<a name="ZH-CN_TOPIC_0000002504091147"></a> 【Description】 IVE module related parameter definition. 【Definition】`
typedef struct { td\_u16 mod\_node\_num; td\_u8 power\_save\_en;
} ot\_ive\_mod\_param;
``` 【Members】

| Member Name | Description |
| --- | --- |
| mod\_node\_num | Number of IVE nodes, range [20, 512]. |
| power\_save\_en | Low power flag, range [0, 1]. |

【Notes】 None. 【Related Data Types and AP Is】 ive\_std\_mod\_init ### ot\_ive\_err\_code 【Description】 Defines error codes. 【Definition】 `typedef enum { OT_IVE_ERR_SYS_TIMEOUT = 0x40, /* IVE process timeout */ OT_IVE_ERR_QUERY_TIMEOUT = 0x41, /* IVE query timeout */ OT_IVE_ERR_BUS_ERR = 0x42, /* IVE BUS error */ OT_IVE_ERR_OPEN_FILE = 0x43, /* IVE open file error */ OT_IVE_ERR_READ_FILE = 0x44, /* IVE read file error */ OT_IVE_ERR_BUTT
} ot_ive_err_code;` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_IVE\_ERR\_SYS\_TIMEOUT | System timeout. |
| OT\_IVE\_ERR\_QUERY\_TIMEOUT | Query timeout. |
| OT\_IVE\_ERR\_BUS\_ERR | Bus error. |
| OT\_IVE\_ERR\_OPEN\_FILE | Failed to open file. |
| OT\_IVE\_ERR\_READ\_FILE | Failed to read file. |

【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_dma\_mode 【Description】 Defines DMA operation mode. 【Definition】 `typedef enum { OT_IVE_DMA_MODE_DIRECT_COPY = 0x0, OT_IVE_DMA_MODE_INTERVAL_COPY = 0x1, OT_IVE_DMA_MODE_SET_3BYTE = 0x2, OT_IVE_DMA_MODE_SET_8BYTE = 0x3, OT_IVE_DMA_MODE_BUTT
} ot_ive_dma_mode;` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_IVE\_DMA\_MODE\_DIRECT\_COPY | Direct fast copy mode. |
| OT\_IVE\_DMA\_MODE\_INTERVAL\_COPY | Interval copy mode. See the ss\_mpi\_ive\_dma [Notes]. |
| OT\_IVE\_DMA\_MODE\_SET\_3BYTE | 3-byte set mode. See the ss\_mpi\_ive\_dma [Notes]. |
| OT\_IVE\_DMA\_MODE\_SET\_8BYTE | 8-byte set mode. See the ss\_mpi\_ive\_dma [Notes]. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_dma\_ctrl](#ot_ive_dma_ctrl) ### ot\_ive\_dma\_ctrl 【Description】 Defines DMA control information. 【Definition】 `typedef struct { ot_ive_dma_mode mode; td_u64 val; td_u8 hor_seg_size; td_u8 elem_size; td_u8 ver_seg_rows;
} ot_ive_dma_ctrl` 【Members】

| Member Name | Description |
| --- | --- |
| mode | DMA operation mode. |
| val | Used only in set mode for memory assignment. 3-byte set mode stores in the lower 3 bytes. |
| hor\_seg\_size | Used only in interval copy mode. The segment size for splitting a row of the source image horizontally. Value range: {2, 3, 4, 8, 16}. |
| elem\_size | Used only in interval copy mode. The first elem\_size bytes of each segment are valid copy fields. Value range: [1, hor\_seg\_size-1]. |
| ver\_seg\_rows | Used only in interval copy mode. Divides the first row of data in every ver\_seg\_rows into segments of hor\_seg\_size, copying the first elem\_size bytes of each segment. Value range: [1, min{65535/src\_stride, src\_height}]. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_dma\_mode](#ot_ive_dma_mode) ### ot\_ive\_filter\_ctrl 【Description】 Defines template filter control information. 【Definition】 `typedef struct { td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter filter coefficient */ td_u8 norm; /* Normalization parameter, by right shift */
} ot_ive_filter_ctrl` 【Members】

| Member Name | Description |
| --- | --- |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. Setting peripheral coefficients to 0 implements 3x3 template filtering. |
| norm | Normalization parameter. Value range: [0, 13]. |

【Notes】 Different filtering effects can be achieved by configuring different template coefficients. 【Related Data Types and AP Is】 None. ### ot\_ive\_csc\_mode 【Description】 Defines color space conversion mode. 【Definition】 `typedef enum { OT_IVE_CSC_MODE_VIDEO_BT601_YUV_TO_RGB = 0x0, /* CSC: YUV_TO_RGB, video transfer mode, RGB value range [16, 235] */ OT_IVE_CSC_MODE_VIDEO_BT709_YUV_TO_RGB = 0x1, /* CSC: YUV_To_RGB, video transfer mode, RGB value range [16, 235] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_RGB = 0x2, /* CSC: YUV_TO_RGB, picture transfer mode, RGB value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_RGB = 0x3, /* CSC: YUV_TO_RGB, picture transfer mode, RGB value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_HSV = 0x4, /* CSC: YUV_TO_HSV, picture transfer mode, HSV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_HSV = 0x5, /* CSC: YUV_TO_HSV, picture transfer mode, HSV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_LAB = 0x6, /* CSC: YUV_TO_LAB, picture transfer mode, Lab value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_LAB = 0x7, /* CSC: YUV_TO_LAB, picture transfer mode, Lab value range [0, 255] */ OT_IVE_CSC_MODE_VIDEO_BT601_RGB_TO_YUV = 0x8, /* CSC: RGB_TO_YUV, video transfer mode, YUV value range [0, 255] */ OT_IVE_CSC_MODE_VIDEO_BT709_RGB_TO_2YUV = 0x9, /* CSC: RGB_TO_YUV, video transfer mode, YUV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_RGB_TO_YUV = 0xa, /* CSC: RGB_TO_YUV, picture transfer mode, Y:[16, 235],U\V:[16, 240] */ OT_IVE_CSC_MODE_PIC_BT709_RGB_TO_YUV = 0xb, /* CSC: RGB_TO_YUV, picture transfer mode, Y:[16, 235],U\V:[16, 240] */ OT_IVE_CSC_MODE_BUTT
} ot_ive_csc_mode` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_YUV\_TO\_RGB | BT601 YUV\_TO\_RGB video conversion. |
| OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_YUV\_TO\_RGB | BT709 YUV\_TO\_RGB video conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_RGB | BT601 YUV\_TO\_RGB picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_RGB | BT709 YUV\_TO\_RGB picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_HSV | BT601 YUV\_TO\_HSV picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_HSV | BT709 YUV\_TO\_HSV picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_LAB | BT601 YUV\_TO\_LAB picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_LAB | BT709 YUV\_TO\_LAB picture conversion. |
| OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_RGB\_TO\_YUV | BT601 RGB\_TO\_YUV video conversion. |
| OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_RGB\_TO\_YUV | BT709 RGB\_TO\_YUV video conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT601\_RGB\_TO\_YUV | BT601 RGB\_TO\_YUV picture conversion. |
| OT\_IVE\_CSC\_MODE\_PIC\_BT709\_RGB\_TO\_YUV | BT709 RGB\_TO\_YUV picture conversion. |

【Notes】 - OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_YUV\_TO\_RGB and OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_YUV\_TO\_RGB modes: output satisfies 16 <= R, G, B <= 235.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_RGB and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_RGB modes: output satisfies 0 <= R, G, B <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_HSV and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_HSV modes: output satisfies 0 <= H, S, V <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_LAB and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_LAB modes: output satisfies 0 <= L, A, B <= 255.
- OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_RGB\_TO\_YUV and OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_RGB\_TO\_YUV modes: output satisfies 0 <= Y, U, V <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_RGB\_TO\_YUV and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_RGB\_TO\_YUV modes: output satisfies Y [16, 235], U/V [16, 240]. 【Related Data Types and AP Is】 - [ot\_ive\_csc\_ctrl](#ot_ive_csc_ctrl)
- [ot\_ive\_filter\_and\_csc\_ctrl](#ot_ive_filter_and_csc_ctrl) ### ot\_ive\_csc\_ctrl 【Description】 Defines color space conversion control information. 【Definition】 `typedef struct { ot_ive_csc_mode mode; /* Working mode */
} ot_ive_csc_ctrl` 【Members】

| Member Name | Description |
| --- | --- |
| mode | Working mode. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_csc\_mode](#ot_ive_csc_mode) ### ot\_ive\_filter\_and\_csc\_ctrl 【Description】 Defines composite template filter plus color space conversion control information. 【Definition】 `typedef struct { ot_ive_csc_mode mode; /* CSC working mode */ td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter filter coefficient */ td_u8 norm; /* Normalization parameter, by right shift */
} ot_ive_filter_and_csc_ctrl ;` 【Members】

| Member Name | Description |
| --- | --- |
| mode | Working mode. |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. |
| norm | Normalization parameter. Value range: [0, 13]. |

【Notes】 Only supports 4 modes of YUV2RGB. 【Related Data Types and AP Is】 [ot\_ive\_csc\_mode](#ot_ive_csc_mode) ### ot\_ive\_sobel\_out\_ctrl 【Description】 Defines sobel output control information. 【Definition】 `typedef enum { OT_IVE_SOBEL_OUT_CTRL_BOTH = 0x0, /* Output horizontal and vertical */ OT_IVE_SOBEL_OUT_CTRL_HOR = 0x1, /* Output horizontal */ OT_IVE_SOBEL_OUT_CTRL_VER = 0x2, /* Output vertical */ OT_IVE_SOBEL_OUT_CTRL_BUTT
} ot_ive_sobel_out_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_IVE\_SOBEL\_OUT\_CTRL\_BOTH | Output filtering results using both the template and transposed template simultaneously. |
| OT\_IVE\_SOBEL\_OUT\_CTRL\_HOR | Output only the result of direct template filtering. |
| OT\_IVE\_SOBEL\_OUT\_CTRL\_VER | Output only the result of transposed template filtering. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_sobel\_ctrl](#ot_ive_sobel_ctrl) ### ot\_ive\_sobel\_ctrl 【Description】 Defines sobel-like gradient calculation control information. 【Definition】 `typedef struct { ot_ive_sobel_out_ctrl out_ctrl; /* Output format */ td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter */
} ot_ive_sobel_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| out\_ctrl | Output control enumeration parameter. |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_sobel\_out\_ctrl](#ot_ive_sobel_out_ctrl) ### ot\_ive\_mag\_and\_ang\_out\_ctrl 【Description】 Defines the output format for gradient magnitude and angle calculation. 【Definition】 `typedef enum { OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG = 0x0,/* Only the magnitude is output.*/ OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG_AND_ANG = 0x1, /* The magnitude and angle are output.*/ OT_IVE_MAG_AND_ANG_OUT_CTRL_BUTT
} ot_ive_mag_and_ang_out_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| OT\_IVE\_MAG\_AND\_ANG\_OUT\_CTRL\_MAG | Output magnitude only. |
| OT\_IVE\_MAG\_AND\_ANG\_OUT\_CTRL\_MAG\_AND\_ANG | Output both magnitude and angle. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_mag\_and\_ang\_ctrl](#ot_ive_mag_and_ang_ctrl) ### ot\_ive\_mag\_and\_ang\_ctrl 【Description】 Defines control information for gradient magnitude and angle calculation. 【Definition】 `typedef struct { ot_ive_mag_and_ang_out_ctrl out_ctrl; td_u16 threshld; td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter. */
} ot_ive_mag_and_ang_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| out\_ctrl | Output format. |
| threshold | Threshold for thresholding the magnitude. |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. |

【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_mag\_and\_ang\_out\_ctrl](#ot_ive_mag_and_ang_out_ctrl) ### ot\_ive\_dilate\_ctrl 【Description】 Defines dilation control information. 【Definition】 `typedef struct { td_u8 mask[OT_IVE_MASK_NUM]; /* The template parameter value must be 0 or 255. */
} ot_ive_dilate_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. Value range: 0 or 255. |

【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_erode\_ctrl 【Description】 Defines erosion control information. 【Definition】 `typedef struct { td_u8 mask[OT_IVE_MASK_NUM]; /* The template parameter value must be 0 or 255. */
} ot_ive_erode_ctrl;` 【Members】

| Member Name | Description |
| --- | --- |
| mask[OT\_IVE\_MASK\_NUM] | 5x5 template coefficients. Value: 0 or 255. |

【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_threshold\_mode 【Description】 Defines image binarization output format. 【Definition】 `typedef enum { OT_IVE_THRESHOLD_MODE_BINARY = 0x0, /* src_val <= low_thr, dst_val = min_val; src_val > low_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_TRUNC = 0x1, /* src_val <= low_threshold, dst_val = src_val; src_val > low_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_TO_MIN_VAL = 0x2, /* src_val <= low_threshold, dst_val = min_val; src_val > low_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_MIN_MID_MAX = 0x3, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_ORIG_MID_MAX = 0x4, /* src_val <= low_threshold, dst_val = src_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_MIN_MID_ORI = 0x5, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_MIN_ORIG_MAX = 0x6, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = src_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_ORI_MID_ORIG = 0x7, /* src_val <= low_threshold, dst_val = src_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_BUTT
} ot_ive_threshold_mode;` 【Members】 【Notes】 For calculation formulas, see [Notes] in ss\_mpi\_ive\_threshold. For diagrams, see the 8 thresholding mode diagram. 【Related Data Types and AP Is】 [ot\_ive\_threshold\_ctrl](#ot_ive_threshold_ctrl) ### ot\_ive\_threshold\_ctrl 【Description】 Defines image binarization control information. 【Definition】 `typedef struct { ot_ive_threshold_mode mode; td_u8 low_threshold; /* user-defined threshold, 0<=u8Low Thr<=255 */ td_u8 high_threshold; /* user-defined threshold, if mode<OT_IVE_THRESHOLD_MODE_MIN_MID_MAX, high_threshold is not used, else 0<=low_threshold<= high_threshold <=255; */`

