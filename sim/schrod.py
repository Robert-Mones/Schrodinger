# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\matta\Desktop\CAT Assembly.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'schrod_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('RH Upper Leg.step-1')
body_1.SetPos(chrono.ChVectorD(-0.0504079632019011,0.0866878597372663,0.485552088685124))
body_1.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_1.SetMass(0.136108623403302)
body_1.SetInertiaXX(chrono.ChVectorD(0.000251127199041514,0.000278570511615183,4.3176117457812e-05))
body_1.SetInertiaXY(chrono.ChVectorD(1.42872163391932e-07,3.4559893670804e-06,-6.25413918046308e-06))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.000248663282174205,0.063251113648344,-0.00120904429041014),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.017347807647928,0.082122177814627,-1.31942998193857E-10)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,0.707106781186547,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_2_shape = chrono.ChObjShapeFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1_2_level = chrono.ChAssetLevel() 
body_1_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_2_level.GetAssets().push_back(body_1_2_shape) 
body_1.GetAssets().push_back(body_1_2_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,0.0071)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_1.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999995,0.0071)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_1.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999995,-0.0072)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_1.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_6_shape = chrono.ChObjShapeFile() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_1_6_level = chrono.ChAssetLevel() 
body_1_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_6_level.GetAssets().push_back(body_1_6_shape) 
body_1.GetAssets().push_back(body_1_6_level) 

# Visualization shape 
body_1_7_shape = chrono.ChObjShapeFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1_7_level = chrono.ChAssetLevel() 
body_1_7_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_7_level.GetAssets().push_back(body_1_7_shape) 
body_1.GetAssets().push_back(body_1_7_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,-0.0072)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_1.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_9_shape = chrono.ChObjShapeFile() 
body_1_9_shape.SetFilename(shapes_dir +'body_1_9.obj') 
body_1_9_level = chrono.ChAssetLevel() 
body_1_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_9_level.GetAssets().push_back(body_1_9_shape) 
body_1.GetAssets().push_back(body_1_9_level) 

# Visualization shape 
body_1_10_shape = chrono.ChObjShapeFile() 
body_1_10_shape.SetFilename(shapes_dir +'body_1_10.obj') 
body_1_10_level = chrono.ChAssetLevel() 
body_1_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_10_level.GetAssets().push_back(body_1_10_shape) 
body_1.GetAssets().push_back(body_1_10_level) 

# Visualization shape 
body_1_11_shape = chrono.ChObjShapeFile() 
body_1_11_shape.SetFilename(shapes_dir +'body_1_11.obj') 
body_1_11_level = chrono.ChAssetLevel() 
body_1_11_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_11_level.GetAssets().push_back(body_1_11_shape) 
body_1.GetAssets().push_back(body_1_11_level) 

# Visualization shape 
body_1_12_shape = chrono.ChObjShapeFile() 
body_1_12_shape.SetFilename(shapes_dir +'body_1_12.obj') 
body_1_12_level = chrono.ChAssetLevel() 
body_1_12_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_12_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_12_level.GetAssets().push_back(body_1_12_shape) 
body_1.GetAssets().push_back(body_1_12_level) 

# Visualization shape 
body_1_13_shape = chrono.ChObjShapeFile() 
body_1_13_shape.SetFilename(shapes_dir +'body_1_13.obj') 
body_1_13_level = chrono.ChAssetLevel() 
body_1_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_13_level.GetAssets().push_back(body_1_13_shape) 
body_1.GetAssets().push_back(body_1_13_level) 

# Visualization shape 
body_1_14_shape = chrono.ChObjShapeFile() 
body_1_14_shape.SetFilename(shapes_dir +'body_1_14.obj') 
body_1_14_level = chrono.ChAssetLevel() 
body_1_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_14_level.GetAssets().push_back(body_1_14_shape) 
body_1.GetAssets().push_back(body_1_14_level) 

# Visualization shape 
body_1_15_shape = chrono.ChObjShapeFile() 
body_1_15_shape.SetFilename(shapes_dir +'body_1_15.obj') 
body_1_15_level = chrono.ChAssetLevel() 
body_1_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_15_level.GetAssets().push_back(body_1_15_shape) 
body_1.GetAssets().push_back(body_1_15_level) 

# Visualization shape 
body_1_16_shape = chrono.ChObjShapeFile() 
body_1_16_shape.SetFilename(shapes_dir +'body_1_16.obj') 
body_1_16_level = chrono.ChAssetLevel() 
body_1_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_16_level.GetAssets().push_back(body_1_16_shape) 
body_1.GetAssets().push_back(body_1_16_level) 

# Visualization shape 
body_1_17_shape = chrono.ChObjShapeFile() 
body_1_17_shape.SetFilename(shapes_dir +'body_1_17.obj') 
body_1_17_level = chrono.ChAssetLevel() 
body_1_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_17_level.GetAssets().push_back(body_1_17_shape) 
body_1.GetAssets().push_back(body_1_17_level) 

# Visualization shape 
body_1_18_shape = chrono.ChObjShapeFile() 
body_1_18_shape.SetFilename(shapes_dir +'body_1_18.obj') 
body_1_18_level = chrono.ChAssetLevel() 
body_1_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_18_level.GetAssets().push_back(body_1_18_shape) 
body_1.GetAssets().push_back(body_1_18_level) 

# Visualization shape 
body_1_19_shape = chrono.ChObjShapeFile() 
body_1_19_shape.SetFilename(shapes_dir +'body_1_19.obj') 
body_1_19_level = chrono.ChAssetLevel() 
body_1_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_19_level.GetAssets().push_back(body_1_19_shape) 
body_1.GetAssets().push_back(body_1_19_level) 

# Visualization shape 
body_1_20_shape = chrono.ChObjShapeFile() 
body_1_20_shape.SetFilename(shapes_dir +'body_1_20.obj') 
body_1_20_level = chrono.ChAssetLevel() 
body_1_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_20_level.GetAssets().push_back(body_1_20_shape) 
body_1.GetAssets().push_back(body_1_20_level) 

# Visualization shape 
body_1_21_shape = chrono.ChObjShapeFile() 
body_1_21_shape.SetFilename(shapes_dir +'body_1_21.obj') 
body_1_21_level = chrono.ChAssetLevel() 
body_1_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_21_level.GetAssets().push_back(body_1_21_shape) 
body_1.GetAssets().push_back(body_1_21_level) 

# Visualization shape 
body_1_22_shape = chrono.ChObjShapeFile() 
body_1_22_shape.SetFilename(shapes_dir +'body_1_22.obj') 
body_1_22_level = chrono.ChAssetLevel() 
body_1_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_22_level.GetAssets().push_back(body_1_22_shape) 
body_1.GetAssets().push_back(body_1_22_level) 

# Visualization shape 
body_1_23_shape = chrono.ChObjShapeFile() 
body_1_23_shape.SetFilename(shapes_dir +'body_1_23.obj') 
body_1_23_level = chrono.ChAssetLevel() 
body_1_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_23_level.GetAssets().push_back(body_1_23_shape) 
body_1.GetAssets().push_back(body_1_23_level) 

# Visualization shape 
body_1_24_shape = chrono.ChObjShapeFile() 
body_1_24_shape.SetFilename(shapes_dir +'body_1_24.obj') 
body_1_24_level = chrono.ChAssetLevel() 
body_1_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_24_level.GetAssets().push_back(body_1_24_shape) 
body_1.GetAssets().push_back(body_1_24_level) 

# Visualization shape 
body_1_25_shape = chrono.ChObjShapeFile() 
body_1_25_shape.SetFilename(shapes_dir +'body_1_25.obj') 
body_1_25_level = chrono.ChAssetLevel() 
body_1_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_25_level.GetAssets().push_back(body_1_25_shape) 
body_1.GetAssets().push_back(body_1_25_level) 

# Visualization shape 
body_1_26_shape = chrono.ChObjShapeFile() 
body_1_26_shape.SetFilename(shapes_dir +'body_1_26.obj') 
body_1_26_level = chrono.ChAssetLevel() 
body_1_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_26_level.GetAssets().push_back(body_1_26_shape) 
body_1.GetAssets().push_back(body_1_26_level) 

# Visualization shape 
body_1_27_shape = chrono.ChObjShapeFile() 
body_1_27_shape.SetFilename(shapes_dir +'body_1_27.obj') 
body_1_27_level = chrono.ChAssetLevel() 
body_1_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_27_level.GetAssets().push_back(body_1_27_shape) 
body_1.GetAssets().push_back(body_1_27_level) 

# Visualization shape 
body_1_28_shape = chrono.ChObjShapeFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1_28_level = chrono.ChAssetLevel() 
body_1_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_28_level.GetAssets().push_back(body_1_28_shape) 
body_1.GetAssets().push_back(body_1_28_level) 

# Visualization shape 
body_1_29_shape = chrono.ChObjShapeFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1_29_level = chrono.ChAssetLevel() 
body_1_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_29_level.GetAssets().push_back(body_1_29_shape) 
body_1.GetAssets().push_back(body_1_29_level) 

# Visualization shape 
body_1_30_shape = chrono.ChObjShapeFile() 
body_1_30_shape.SetFilename(shapes_dir +'body_1_30.obj') 
body_1_30_level = chrono.ChAssetLevel() 
body_1_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_30_level.GetAssets().push_back(body_1_30_shape) 
body_1.GetAssets().push_back(body_1_30_level) 

# Visualization shape 
body_1_31_shape = chrono.ChObjShapeFile() 
body_1_31_shape.SetFilename(shapes_dir +'body_1_31.obj') 
body_1_31_level = chrono.ChAssetLevel() 
body_1_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_31_level.GetAssets().push_back(body_1_31_shape) 
body_1.GetAssets().push_back(body_1_31_level) 

# Visualization shape 
body_1_32_shape = chrono.ChObjShapeFile() 
body_1_32_shape.SetFilename(shapes_dir +'body_1_32.obj') 
body_1_32_level = chrono.ChAssetLevel() 
body_1_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_32_level.GetAssets().push_back(body_1_32_shape) 
body_1.GetAssets().push_back(body_1_32_level) 

# Visualization shape 
body_1_33_shape = chrono.ChObjShapeFile() 
body_1_33_shape.SetFilename(shapes_dir +'body_1_33.obj') 
body_1_33_level = chrono.ChAssetLevel() 
body_1_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_33_level.GetAssets().push_back(body_1_33_shape) 
body_1.GetAssets().push_back(body_1_33_level) 

# Visualization shape 
body_1_34_shape = chrono.ChObjShapeFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1_34_level = chrono.ChAssetLevel() 
body_1_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_34_level.GetAssets().push_back(body_1_34_shape) 
body_1.GetAssets().push_back(body_1_34_level) 

# Visualization shape 
body_1_35_shape = chrono.ChObjShapeFile() 
body_1_35_shape.SetFilename(shapes_dir +'body_1_35.obj') 
body_1_35_level = chrono.ChAssetLevel() 
body_1_35_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_35_level.GetAssets().push_back(body_1_35_shape) 
body_1.GetAssets().push_back(body_1_35_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,-0.00389999999999999)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_37_shape = chrono.ChObjShapeFile() 
body_1_37_shape.SetFilename(shapes_dir +'body_1_37.obj') 
body_1_37_level = chrono.ChAssetLevel() 
body_1_37_level.GetFrame().SetPos(chrono.ChVectorD(0.0332,0.00700000585427701,-5.01644618989966E-05)) 
body_1_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_37_level.GetAssets().push_back(body_1_37_shape) 
body_1.GetAssets().push_back(body_1_37_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,-0.01255)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.47487373415292E-15,-2.47487373415292E-15,0.707106781186547)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_1.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_39_shape = chrono.ChObjShapeFile() 
body_1_39_shape.SetFilename(shapes_dir +'body_1_39.obj') 
body_1_39_level = chrono.ChAssetLevel() 
body_1_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_39_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_39_level.GetAssets().push_back(body_1_39_shape) 
body_1.GetAssets().push_back(body_1_39_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(-6.93889390390723E-18,0.05897405927155,-0.0039)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_41_shape = chrono.ChObjShapeFile() 
body_1_41_shape.SetFilename(shapes_dir +'body_1_41.obj') 
body_1_41_level = chrono.ChAssetLevel() 
body_1_41_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,0.14,0.02)) 
body_1_41_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_41_level.GetAssets().push_back(body_1_41_shape) 
body_1.GetAssets().push_back(body_1_41_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(-0.026097807647928,0.082122177814627,-1.31942998193857E-10)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_1.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(-6.93889390390723E-18,0.05897405927155,-0.01255)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.82842712474619E-15,-2.82842712474619E-15,0.707106781186547)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_1.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02055,0.00700000585427696,-5.01644618989966E-05)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_45_shape = chrono.ChObjShapeFile() 
body_1_45_shape.SetFilename(shapes_dir +'body_1_45.obj') 
body_1_45_level = chrono.ChAssetLevel() 
body_1_45_level.GetFrame().SetPos(chrono.ChVectorD(0.02555,0.14,0.02)) 
body_1_45_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186551,0,0,-0.707106781186544)) 
body_1_45_level.GetAssets().push_back(body_1_45_shape) 
body_1.GetAssets().push_back(body_1_45_level) 

# Visualization shape 
body_1_46_shape = chrono.ChObjShapeFile() 
body_1_46_shape.SetFilename(shapes_dir +'body_1_46.obj') 
body_1_46_level = chrono.ChAssetLevel() 
body_1_46_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_46_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_46_level.GetAssets().push_back(body_1_46_shape) 
body_1.GetAssets().push_back(body_1_46_level) 

# Visualization shape 
body_1_47_shape = chrono.ChObjShapeFile() 
body_1_47_shape.SetFilename(shapes_dir +'body_1_47.obj') 
body_1_47_level = chrono.ChAssetLevel() 
body_1_47_level.GetFrame().SetPos(chrono.ChVectorD(-0.02655,0.14811829320711,0.022820012245991)) 
body_1_47_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,0.5,0.5,0.5)) 
body_1_47_level.GetAssets().push_back(body_1_47_shape) 
body_1.GetAssets().push_back(body_1_47_level) 

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('RH Upper Leg.step-2')
body_2.SetPos(chrono.ChVectorD(-0.0504079632018997,0.0868378597372612,0.244052088685124))
body_2.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_2.SetMass(0.136108623403302)
body_2.SetInertiaXX(chrono.ChVectorD(0.000251127199041514,0.000278570511615183,4.3176117457812e-05))
body_2.SetInertiaXY(chrono.ChVectorD(1.42872163391932e-07,3.4559893670804e-06,-6.25413918046307e-06))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.000248663282174205,0.063251113648344,-0.00120904429041014),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.017347807647928,0.082122177814627,-1.31942984316069E-10)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,0.707106781186547,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_2_shape = chrono.ChObjShapeFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1_2_level = chrono.ChAssetLevel() 
body_1_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_2_level.GetAssets().push_back(body_1_2_shape) 
body_2.GetAssets().push_back(body_1_2_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,0.00710000000000001)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_2.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000550000000000023,0.00710000000000001)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_2.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999995,-0.00719999999999998)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_2.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_2_6_shape = chrono.ChObjShapeFile() 
body_2_6_shape.SetFilename(shapes_dir +'body_2_6.obj') 
body_2_6_level = chrono.ChAssetLevel() 
body_2_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_2_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_2_6_level.GetAssets().push_back(body_2_6_shape) 
body_2.GetAssets().push_back(body_2_6_level) 

# Visualization shape 
body_1_7_shape = chrono.ChObjShapeFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1_7_level = chrono.ChAssetLevel() 
body_1_7_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_7_level.GetAssets().push_back(body_1_7_shape) 
body_2.GetAssets().push_back(body_1_7_level) 

# Visualization shape 
body_1_3_shape = chrono.ChObjShapeFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1_3_level = chrono.ChAssetLevel() 
body_1_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,-0.00719999999999998)) 
body_1_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_1_3_level.GetAssets().push_back(body_1_3_shape) 
body_2.GetAssets().push_back(body_1_3_level) 

# Visualization shape 
body_1_9_shape = chrono.ChObjShapeFile() 
body_1_9_shape.SetFilename(shapes_dir +'body_1_9.obj') 
body_1_9_level = chrono.ChAssetLevel() 
body_1_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_9_level.GetAssets().push_back(body_1_9_shape) 
body_2.GetAssets().push_back(body_1_9_level) 

# Visualization shape 
body_1_10_shape = chrono.ChObjShapeFile() 
body_1_10_shape.SetFilename(shapes_dir +'body_1_10.obj') 
body_1_10_level = chrono.ChAssetLevel() 
body_1_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_10_level.GetAssets().push_back(body_1_10_shape) 
body_2.GetAssets().push_back(body_1_10_level) 

# Visualization shape 
body_1_11_shape = chrono.ChObjShapeFile() 
body_1_11_shape.SetFilename(shapes_dir +'body_1_11.obj') 
body_1_11_level = chrono.ChAssetLevel() 
body_1_11_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_11_level.GetAssets().push_back(body_1_11_shape) 
body_2.GetAssets().push_back(body_1_11_level) 

# Visualization shape 
body_1_12_shape = chrono.ChObjShapeFile() 
body_1_12_shape.SetFilename(shapes_dir +'body_1_12.obj') 
body_1_12_level = chrono.ChAssetLevel() 
body_1_12_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_12_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_12_level.GetAssets().push_back(body_1_12_shape) 
body_2.GetAssets().push_back(body_1_12_level) 

# Visualization shape 
body_1_13_shape = chrono.ChObjShapeFile() 
body_1_13_shape.SetFilename(shapes_dir +'body_1_13.obj') 
body_1_13_level = chrono.ChAssetLevel() 
body_1_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_13_level.GetAssets().push_back(body_1_13_shape) 
body_2.GetAssets().push_back(body_1_13_level) 

# Visualization shape 
body_1_14_shape = chrono.ChObjShapeFile() 
body_1_14_shape.SetFilename(shapes_dir +'body_1_14.obj') 
body_1_14_level = chrono.ChAssetLevel() 
body_1_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_14_level.GetAssets().push_back(body_1_14_shape) 
body_2.GetAssets().push_back(body_1_14_level) 

# Visualization shape 
body_1_15_shape = chrono.ChObjShapeFile() 
body_1_15_shape.SetFilename(shapes_dir +'body_1_15.obj') 
body_1_15_level = chrono.ChAssetLevel() 
body_1_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_15_level.GetAssets().push_back(body_1_15_shape) 
body_2.GetAssets().push_back(body_1_15_level) 

# Visualization shape 
body_1_16_shape = chrono.ChObjShapeFile() 
body_1_16_shape.SetFilename(shapes_dir +'body_1_16.obj') 
body_1_16_level = chrono.ChAssetLevel() 
body_1_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_16_level.GetAssets().push_back(body_1_16_shape) 
body_2.GetAssets().push_back(body_1_16_level) 

# Visualization shape 
body_1_17_shape = chrono.ChObjShapeFile() 
body_1_17_shape.SetFilename(shapes_dir +'body_1_17.obj') 
body_1_17_level = chrono.ChAssetLevel() 
body_1_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_17_level.GetAssets().push_back(body_1_17_shape) 
body_2.GetAssets().push_back(body_1_17_level) 

# Visualization shape 
body_1_18_shape = chrono.ChObjShapeFile() 
body_1_18_shape.SetFilename(shapes_dir +'body_1_18.obj') 
body_1_18_level = chrono.ChAssetLevel() 
body_1_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_18_level.GetAssets().push_back(body_1_18_shape) 
body_2.GetAssets().push_back(body_1_18_level) 

# Visualization shape 
body_1_19_shape = chrono.ChObjShapeFile() 
body_1_19_shape.SetFilename(shapes_dir +'body_1_19.obj') 
body_1_19_level = chrono.ChAssetLevel() 
body_1_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_19_level.GetAssets().push_back(body_1_19_shape) 
body_2.GetAssets().push_back(body_1_19_level) 

# Visualization shape 
body_1_20_shape = chrono.ChObjShapeFile() 
body_1_20_shape.SetFilename(shapes_dir +'body_1_20.obj') 
body_1_20_level = chrono.ChAssetLevel() 
body_1_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_20_level.GetAssets().push_back(body_1_20_shape) 
body_2.GetAssets().push_back(body_1_20_level) 

# Visualization shape 
body_1_21_shape = chrono.ChObjShapeFile() 
body_1_21_shape.SetFilename(shapes_dir +'body_1_21.obj') 
body_1_21_level = chrono.ChAssetLevel() 
body_1_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_21_level.GetAssets().push_back(body_1_21_shape) 
body_2.GetAssets().push_back(body_1_21_level) 

# Visualization shape 
body_1_22_shape = chrono.ChObjShapeFile() 
body_1_22_shape.SetFilename(shapes_dir +'body_1_22.obj') 
body_1_22_level = chrono.ChAssetLevel() 
body_1_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_22_level.GetAssets().push_back(body_1_22_shape) 
body_2.GetAssets().push_back(body_1_22_level) 

# Visualization shape 
body_1_23_shape = chrono.ChObjShapeFile() 
body_1_23_shape.SetFilename(shapes_dir +'body_1_23.obj') 
body_1_23_level = chrono.ChAssetLevel() 
body_1_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_23_level.GetAssets().push_back(body_1_23_shape) 
body_2.GetAssets().push_back(body_1_23_level) 

# Visualization shape 
body_1_24_shape = chrono.ChObjShapeFile() 
body_1_24_shape.SetFilename(shapes_dir +'body_1_24.obj') 
body_1_24_level = chrono.ChAssetLevel() 
body_1_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_24_level.GetAssets().push_back(body_1_24_shape) 
body_2.GetAssets().push_back(body_1_24_level) 

# Visualization shape 
body_1_25_shape = chrono.ChObjShapeFile() 
body_1_25_shape.SetFilename(shapes_dir +'body_1_25.obj') 
body_1_25_level = chrono.ChAssetLevel() 
body_1_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_25_level.GetAssets().push_back(body_1_25_shape) 
body_2.GetAssets().push_back(body_1_25_level) 

# Visualization shape 
body_1_26_shape = chrono.ChObjShapeFile() 
body_1_26_shape.SetFilename(shapes_dir +'body_1_26.obj') 
body_1_26_level = chrono.ChAssetLevel() 
body_1_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_26_level.GetAssets().push_back(body_1_26_shape) 
body_2.GetAssets().push_back(body_1_26_level) 

# Visualization shape 
body_1_27_shape = chrono.ChObjShapeFile() 
body_1_27_shape.SetFilename(shapes_dir +'body_1_27.obj') 
body_1_27_level = chrono.ChAssetLevel() 
body_1_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_27_level.GetAssets().push_back(body_1_27_shape) 
body_2.GetAssets().push_back(body_1_27_level) 

# Visualization shape 
body_1_28_shape = chrono.ChObjShapeFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1_28_level = chrono.ChAssetLevel() 
body_1_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_28_level.GetAssets().push_back(body_1_28_shape) 
body_2.GetAssets().push_back(body_1_28_level) 

# Visualization shape 
body_1_29_shape = chrono.ChObjShapeFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1_29_level = chrono.ChAssetLevel() 
body_1_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_29_level.GetAssets().push_back(body_1_29_shape) 
body_2.GetAssets().push_back(body_1_29_level) 

# Visualization shape 
body_1_30_shape = chrono.ChObjShapeFile() 
body_1_30_shape.SetFilename(shapes_dir +'body_1_30.obj') 
body_1_30_level = chrono.ChAssetLevel() 
body_1_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_30_level.GetAssets().push_back(body_1_30_shape) 
body_2.GetAssets().push_back(body_1_30_level) 

# Visualization shape 
body_1_31_shape = chrono.ChObjShapeFile() 
body_1_31_shape.SetFilename(shapes_dir +'body_1_31.obj') 
body_1_31_level = chrono.ChAssetLevel() 
body_1_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_31_level.GetAssets().push_back(body_1_31_shape) 
body_2.GetAssets().push_back(body_1_31_level) 

# Visualization shape 
body_1_32_shape = chrono.ChObjShapeFile() 
body_1_32_shape.SetFilename(shapes_dir +'body_1_32.obj') 
body_1_32_level = chrono.ChAssetLevel() 
body_1_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_32_level.GetAssets().push_back(body_1_32_shape) 
body_2.GetAssets().push_back(body_1_32_level) 

# Visualization shape 
body_1_33_shape = chrono.ChObjShapeFile() 
body_1_33_shape.SetFilename(shapes_dir +'body_1_33.obj') 
body_1_33_level = chrono.ChAssetLevel() 
body_1_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_33_level.GetAssets().push_back(body_1_33_shape) 
body_2.GetAssets().push_back(body_1_33_level) 

# Visualization shape 
body_1_34_shape = chrono.ChObjShapeFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1_34_level = chrono.ChAssetLevel() 
body_1_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_34_level.GetAssets().push_back(body_1_34_shape) 
body_2.GetAssets().push_back(body_1_34_level) 

# Visualization shape 
body_1_35_shape = chrono.ChObjShapeFile() 
body_1_35_shape.SetFilename(shapes_dir +'body_1_35.obj') 
body_1_35_level = chrono.ChAssetLevel() 
body_1_35_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,-4.99999999999945E-05)) 
body_1_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_35_level.GetAssets().push_back(body_1_35_shape) 
body_2.GetAssets().push_back(body_1_35_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,-0.00389999999999999)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_37_shape = chrono.ChObjShapeFile() 
body_1_37_shape.SetFilename(shapes_dir +'body_1_37.obj') 
body_1_37_level = chrono.ChAssetLevel() 
body_1_37_level.GetFrame().SetPos(chrono.ChVectorD(0.0332,0.00700000585427699,-5.01644618989827E-05)) 
body_1_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_37_level.GetAssets().push_back(body_1_37_shape) 
body_2.GetAssets().push_back(body_1_37_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,-0.01255)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.47487373415292E-15,-2.47487373415292E-15,0.707106781186547)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_2.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_39_shape = chrono.ChObjShapeFile() 
body_1_39_shape.SetFilename(shapes_dir +'body_1_39.obj') 
body_1_39_level = chrono.ChAssetLevel() 
body_1_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_39_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_39_level.GetAssets().push_back(body_1_39_shape) 
body_2.GetAssets().push_back(body_1_39_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(-6.93889390390723E-18,0.05897405927155,-0.00389999999999999)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_41_shape = chrono.ChObjShapeFile() 
body_1_41_shape.SetFilename(shapes_dir +'body_1_41.obj') 
body_1_41_level = chrono.ChAssetLevel() 
body_1_41_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,0.14,0.02)) 
body_1_41_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_41_level.GetAssets().push_back(body_1_41_shape) 
body_2.GetAssets().push_back(body_1_41_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(-0.026097807647928,0.082122177814627,-1.31942984316069E-10)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_2.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_38_shape = chrono.ChObjShapeFile() 
body_1_38_shape.SetFilename(shapes_dir +'body_1_38.obj') 
body_1_38_level = chrono.ChAssetLevel() 
body_1_38_level.GetFrame().SetPos(chrono.ChVectorD(-6.93889390390723E-18,0.05897405927155,-0.01255)) 
body_1_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.82842712474619E-15,-2.82842712474619E-15,0.707106781186547)) 
body_1_38_level.GetAssets().push_back(body_1_38_shape) 
body_2.GetAssets().push_back(body_1_38_level) 

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02055,0.00700000585427699,-5.01644618989827E-05)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

# Visualization shape 
body_1_45_shape = chrono.ChObjShapeFile() 
body_1_45_shape.SetFilename(shapes_dir +'body_1_45.obj') 
body_1_45_level = chrono.ChAssetLevel() 
body_1_45_level.GetFrame().SetPos(chrono.ChVectorD(0.02555,0.14,0.02)) 
body_1_45_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186551,0,0,-0.707106781186544)) 
body_1_45_level.GetAssets().push_back(body_1_45_shape) 
body_2.GetAssets().push_back(body_1_45_level) 

# Visualization shape 
body_1_46_shape = chrono.ChObjShapeFile() 
body_1_46_shape.SetFilename(shapes_dir +'body_1_46.obj') 
body_1_46_level = chrono.ChAssetLevel() 
body_1_46_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_46_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_46_level.GetAssets().push_back(body_1_46_shape) 
body_2.GetAssets().push_back(body_1_46_level) 

# Visualization shape 
body_1_47_shape = chrono.ChObjShapeFile() 
body_1_47_shape.SetFilename(shapes_dir +'body_1_47.obj') 
body_1_47_level = chrono.ChAssetLevel() 
body_1_47_level.GetFrame().SetPos(chrono.ChVectorD(-0.02655,0.14811829320711,0.022820012245991)) 
body_1_47_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,0.5,0.5,0.5)) 
body_1_47_level.GetAssets().push_back(body_1_47_shape) 
body_2.GetAssets().push_back(body_1_47_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('RH Lower Leg.step-2')
body_3.SetPos(chrono.ChVectorD(-0.0504079632018998,0.0868878597372611,0.24405208868513))
body_3.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_3.SetMass(0.0965206572697057)
body_3.SetInertiaXX(chrono.ChVectorD(0.000185081309306375,0.000191945535962297,1.37689080285943e-05))
body_3.SetInertiaXY(chrono.ChVectorD(8.26883059237437e-09,-1.85046318451561e-06,-5.63845786502872e-07))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000646350768908585,0.0946708494136033,0.0216226115976762),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_3.GetAssets().push_back(body_3_1_level) 

# Visualization shape 
body_3_2_shape = chrono.ChObjShapeFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_3_2_level = chrono.ChAssetLevel() 
body_3_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_2_level.GetAssets().push_back(body_3_2_shape) 
body_3.GetAssets().push_back(body_3_2_level) 

# Visualization shape 
body_3_3_shape = chrono.ChObjShapeFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_3_3_level = chrono.ChAssetLevel() 
body_3_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_3_level.GetAssets().push_back(body_3_3_shape) 
body_3.GetAssets().push_back(body_3_3_level) 

# Visualization shape 
body_3_4_shape = chrono.ChObjShapeFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3_4_level = chrono.ChAssetLevel() 
body_3_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_4_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_4_level.GetAssets().push_back(body_3_4_shape) 
body_3.GetAssets().push_back(body_3_4_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,0.0129)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_3.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,0.0272)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_3.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_7_shape = chrono.ChObjShapeFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_3_7_level = chrono.ChAssetLevel() 
body_3_7_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_7_level.GetAssets().push_back(body_3_7_shape) 
body_3.GetAssets().push_back(body_3_7_level) 

# Visualization shape 
body_3_8_shape = chrono.ChObjShapeFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3_8_level = chrono.ChAssetLevel() 
body_3_8_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_8_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_8_level.GetAssets().push_back(body_3_8_shape) 
body_3.GetAssets().push_back(body_3_8_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,0.0129)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_3.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_10_shape = chrono.ChObjShapeFile() 
body_3_10_shape.SetFilename(shapes_dir +'body_3_10.obj') 
body_3_10_level = chrono.ChAssetLevel() 
body_3_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_10_level.GetAssets().push_back(body_3_10_shape) 
body_3.GetAssets().push_back(body_3_10_level) 

# Visualization shape 
body_3_11_shape = chrono.ChObjShapeFile() 
body_3_11_shape.SetFilename(shapes_dir +'body_3_11.obj') 
body_3_11_level = chrono.ChAssetLevel() 
body_3_11_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_11_level.GetAssets().push_back(body_3_11_shape) 
body_3.GetAssets().push_back(body_3_11_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,0.0272)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_3.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_13_shape = chrono.ChObjShapeFile() 
body_3_13_shape.SetFilename(shapes_dir +'body_3_13.obj') 
body_3_13_level = chrono.ChAssetLevel() 
body_3_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_13_level.GetAssets().push_back(body_3_13_shape) 
body_3.GetAssets().push_back(body_3_13_level) 

# Visualization shape 
body_3_14_shape = chrono.ChObjShapeFile() 
body_3_14_shape.SetFilename(shapes_dir +'body_3_14.obj') 
body_3_14_level = chrono.ChAssetLevel() 
body_3_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_14_level.GetAssets().push_back(body_3_14_shape) 
body_3.GetAssets().push_back(body_3_14_level) 

# Visualization shape 
body_3_15_shape = chrono.ChObjShapeFile() 
body_3_15_shape.SetFilename(shapes_dir +'body_3_15.obj') 
body_3_15_level = chrono.ChAssetLevel() 
body_3_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_15_level.GetAssets().push_back(body_3_15_shape) 
body_3.GetAssets().push_back(body_3_15_level) 

# Visualization shape 
body_3_16_shape = chrono.ChObjShapeFile() 
body_3_16_shape.SetFilename(shapes_dir +'body_3_16.obj') 
body_3_16_level = chrono.ChAssetLevel() 
body_3_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_16_level.GetAssets().push_back(body_3_16_shape) 
body_3.GetAssets().push_back(body_3_16_level) 

# Visualization shape 
body_3_17_shape = chrono.ChObjShapeFile() 
body_3_17_shape.SetFilename(shapes_dir +'body_3_17.obj') 
body_3_17_level = chrono.ChAssetLevel() 
body_3_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_17_level.GetAssets().push_back(body_3_17_shape) 
body_3.GetAssets().push_back(body_3_17_level) 

# Visualization shape 
body_3_18_shape = chrono.ChObjShapeFile() 
body_3_18_shape.SetFilename(shapes_dir +'body_3_18.obj') 
body_3_18_level = chrono.ChAssetLevel() 
body_3_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_18_level.GetAssets().push_back(body_3_18_shape) 
body_3.GetAssets().push_back(body_3_18_level) 

# Visualization shape 
body_3_19_shape = chrono.ChObjShapeFile() 
body_3_19_shape.SetFilename(shapes_dir +'body_3_19.obj') 
body_3_19_level = chrono.ChAssetLevel() 
body_3_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_19_level.GetAssets().push_back(body_3_19_shape) 
body_3.GetAssets().push_back(body_3_19_level) 

# Visualization shape 
body_3_20_shape = chrono.ChObjShapeFile() 
body_3_20_shape.SetFilename(shapes_dir +'body_3_20.obj') 
body_3_20_level = chrono.ChAssetLevel() 
body_3_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_20_level.GetAssets().push_back(body_3_20_shape) 
body_3.GetAssets().push_back(body_3_20_level) 

# Visualization shape 
body_3_21_shape = chrono.ChObjShapeFile() 
body_3_21_shape.SetFilename(shapes_dir +'body_3_21.obj') 
body_3_21_level = chrono.ChAssetLevel() 
body_3_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_21_level.GetAssets().push_back(body_3_21_shape) 
body_3.GetAssets().push_back(body_3_21_level) 

# Visualization shape 
body_3_22_shape = chrono.ChObjShapeFile() 
body_3_22_shape.SetFilename(shapes_dir +'body_3_22.obj') 
body_3_22_level = chrono.ChAssetLevel() 
body_3_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_22_level.GetAssets().push_back(body_3_22_shape) 
body_3.GetAssets().push_back(body_3_22_level) 

# Visualization shape 
body_3_23_shape = chrono.ChObjShapeFile() 
body_3_23_shape.SetFilename(shapes_dir +'body_3_23.obj') 
body_3_23_level = chrono.ChAssetLevel() 
body_3_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_23_level.GetAssets().push_back(body_3_23_shape) 
body_3.GetAssets().push_back(body_3_23_level) 

# Visualization shape 
body_3_24_shape = chrono.ChObjShapeFile() 
body_3_24_shape.SetFilename(shapes_dir +'body_3_24.obj') 
body_3_24_level = chrono.ChAssetLevel() 
body_3_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_24_level.GetAssets().push_back(body_3_24_shape) 
body_3.GetAssets().push_back(body_3_24_level) 

# Visualization shape 
body_3_25_shape = chrono.ChObjShapeFile() 
body_3_25_shape.SetFilename(shapes_dir +'body_3_25.obj') 
body_3_25_level = chrono.ChAssetLevel() 
body_3_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_25_level.GetAssets().push_back(body_3_25_shape) 
body_3.GetAssets().push_back(body_3_25_level) 

# Visualization shape 
body_3_26_shape = chrono.ChObjShapeFile() 
body_3_26_shape.SetFilename(shapes_dir +'body_3_26.obj') 
body_3_26_level = chrono.ChAssetLevel() 
body_3_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_26_level.GetAssets().push_back(body_3_26_shape) 
body_3.GetAssets().push_back(body_3_26_level) 

# Visualization shape 
body_3_27_shape = chrono.ChObjShapeFile() 
body_3_27_shape.SetFilename(shapes_dir +'body_3_27.obj') 
body_3_27_level = chrono.ChAssetLevel() 
body_3_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_27_level.GetAssets().push_back(body_3_27_shape) 
body_3.GetAssets().push_back(body_3_27_level) 

# Visualization shape 
body_3_28_shape = chrono.ChObjShapeFile() 
body_3_28_shape.SetFilename(shapes_dir +'body_3_28.obj') 
body_3_28_level = chrono.ChAssetLevel() 
body_3_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_28_level.GetAssets().push_back(body_3_28_shape) 
body_3.GetAssets().push_back(body_3_28_level) 

# Visualization shape 
body_3_29_shape = chrono.ChObjShapeFile() 
body_3_29_shape.SetFilename(shapes_dir +'body_3_29.obj') 
body_3_29_level = chrono.ChAssetLevel() 
body_3_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_29_level.GetAssets().push_back(body_3_29_shape) 
body_3.GetAssets().push_back(body_3_29_level) 

# Visualization shape 
body_3_30_shape = chrono.ChObjShapeFile() 
body_3_30_shape.SetFilename(shapes_dir +'body_3_30.obj') 
body_3_30_level = chrono.ChAssetLevel() 
body_3_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_30_level.GetAssets().push_back(body_3_30_shape) 
body_3.GetAssets().push_back(body_3_30_level) 

# Visualization shape 
body_3_31_shape = chrono.ChObjShapeFile() 
body_3_31_shape.SetFilename(shapes_dir +'body_3_31.obj') 
body_3_31_level = chrono.ChAssetLevel() 
body_3_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_31_level.GetAssets().push_back(body_3_31_shape) 
body_3.GetAssets().push_back(body_3_31_level) 

# Visualization shape 
body_3_32_shape = chrono.ChObjShapeFile() 
body_3_32_shape.SetFilename(shapes_dir +'body_3_32.obj') 
body_3_32_level = chrono.ChAssetLevel() 
body_3_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_32_level.GetAssets().push_back(body_3_32_shape) 
body_3.GetAssets().push_back(body_3_32_level) 

# Visualization shape 
body_3_33_shape = chrono.ChObjShapeFile() 
body_3_33_shape.SetFilename(shapes_dir +'body_3_33.obj') 
body_3_33_level = chrono.ChAssetLevel() 
body_3_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_33_level.GetAssets().push_back(body_3_33_shape) 
body_3.GetAssets().push_back(body_3_33_level) 

# Visualization shape 
body_3_34_shape = chrono.ChObjShapeFile() 
body_3_34_shape.SetFilename(shapes_dir +'body_3_34.obj') 
body_3_34_level = chrono.ChAssetLevel() 
body_3_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_34_level.GetAssets().push_back(body_3_34_shape) 
body_3.GetAssets().push_back(body_3_34_level) 

# Visualization shape 
body_3_35_shape = chrono.ChObjShapeFile() 
body_3_35_shape.SetFilename(shapes_dir +'body_3_35.obj') 
body_3_35_level = chrono.ChAssetLevel() 
body_3_35_level.GetFrame().SetPos(chrono.ChVectorD(0.0302,0.140000131576897,0.020050271710659)) 
body_3_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_3_35_level.GetAssets().push_back(body_3_35_shape) 
body_3.GetAssets().push_back(body_3_35_level) 

# Visualization shape 
body_3_36_shape = chrono.ChObjShapeFile() 
body_3_36_shape.SetFilename(shapes_dir +'body_3_36.obj') 
body_3_36_level = chrono.ChAssetLevel() 
body_3_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_36_level.GetAssets().push_back(body_3_36_shape) 
body_3.GetAssets().push_back(body_3_36_level) 

# Visualization shape 
body_3_37_shape = chrono.ChObjShapeFile() 
body_3_37_shape.SetFilename(shapes_dir +'body_3_37.obj') 
body_3_37_level = chrono.ChAssetLevel() 
body_3_37_level.GetFrame().SetPos(chrono.ChVectorD(0.01855,0.140000131576897,0.020050271710659)) 
body_3_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_3_37_level.GetAssets().push_back(body_3_37_shape) 
body_3.GetAssets().push_back(body_3_37_level) 

# Visualization shape 
body_3_38_shape = chrono.ChObjShapeFile() 
body_3_38_shape.SetFilename(shapes_dir +'body_3_38.obj') 
body_3_38_level = chrono.ChAssetLevel() 
body_3_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_38_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_38_level.GetAssets().push_back(body_3_38_shape) 
body_3.GetAssets().push_back(body_3_38_level) 

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('RH Lower Leg.step-1')
body_4.SetPos(chrono.ChVectorD(-0.0504079632019014,0.0867378597372666,0.48555208868513))
body_4.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_4.SetMass(0.0965206572697057)
body_4.SetInertiaXX(chrono.ChVectorD(0.000185081309306375,0.000191945535962297,1.37689080285943e-05))
body_4.SetInertiaXY(chrono.ChVectorD(8.2688305923752e-09,-1.85046318451561e-06,-5.63845786502873e-07))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000646350768908588,0.0946708494136034,0.0216226115976762),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_4.GetAssets().push_back(body_3_1_level) 

# Visualization shape 
body_3_2_shape = chrono.ChObjShapeFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_3_2_level = chrono.ChAssetLevel() 
body_3_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_2_level.GetAssets().push_back(body_3_2_shape) 
body_4.GetAssets().push_back(body_3_2_level) 

# Visualization shape 
body_3_3_shape = chrono.ChObjShapeFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_3_3_level = chrono.ChAssetLevel() 
body_3_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_3_level.GetAssets().push_back(body_3_3_shape) 
body_4.GetAssets().push_back(body_3_3_level) 

# Visualization shape 
body_3_4_shape = chrono.ChObjShapeFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3_4_level = chrono.ChAssetLevel() 
body_3_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_4_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_4_level.GetAssets().push_back(body_3_4_shape) 
body_4.GetAssets().push_back(body_3_4_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,0.0129)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_4.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,0.0272)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_4.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_7_shape = chrono.ChObjShapeFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_3_7_level = chrono.ChAssetLevel() 
body_3_7_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_7_level.GetAssets().push_back(body_3_7_shape) 
body_4.GetAssets().push_back(body_3_7_level) 

# Visualization shape 
body_3_8_shape = chrono.ChObjShapeFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3_8_level = chrono.ChAssetLevel() 
body_3_8_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_8_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_8_level.GetAssets().push_back(body_3_8_shape) 
body_4.GetAssets().push_back(body_3_8_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,0.0129)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_4.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_10_shape = chrono.ChObjShapeFile() 
body_3_10_shape.SetFilename(shapes_dir +'body_3_10.obj') 
body_3_10_level = chrono.ChAssetLevel() 
body_3_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_10_level.GetAssets().push_back(body_3_10_shape) 
body_4.GetAssets().push_back(body_3_10_level) 

# Visualization shape 
body_4_11_shape = chrono.ChObjShapeFile() 
body_4_11_shape.SetFilename(shapes_dir +'body_4_11.obj') 
body_4_11_level = chrono.ChAssetLevel() 
body_4_11_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_4_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_4_11_level.GetAssets().push_back(body_4_11_shape) 
body_4.GetAssets().push_back(body_4_11_level) 

# Visualization shape 
body_3_5_shape = chrono.ChObjShapeFile() 
body_3_5_shape.SetFilename(shapes_dir +'body_3_5.obj') 
body_3_5_level = chrono.ChAssetLevel() 
body_3_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,0.0272)) 
body_3_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_3_5_level.GetAssets().push_back(body_3_5_shape) 
body_4.GetAssets().push_back(body_3_5_level) 

# Visualization shape 
body_3_13_shape = chrono.ChObjShapeFile() 
body_3_13_shape.SetFilename(shapes_dir +'body_3_13.obj') 
body_3_13_level = chrono.ChAssetLevel() 
body_3_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_13_level.GetAssets().push_back(body_3_13_shape) 
body_4.GetAssets().push_back(body_3_13_level) 

# Visualization shape 
body_3_14_shape = chrono.ChObjShapeFile() 
body_3_14_shape.SetFilename(shapes_dir +'body_3_14.obj') 
body_3_14_level = chrono.ChAssetLevel() 
body_3_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_14_level.GetAssets().push_back(body_3_14_shape) 
body_4.GetAssets().push_back(body_3_14_level) 

# Visualization shape 
body_3_15_shape = chrono.ChObjShapeFile() 
body_3_15_shape.SetFilename(shapes_dir +'body_3_15.obj') 
body_3_15_level = chrono.ChAssetLevel() 
body_3_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_15_level.GetAssets().push_back(body_3_15_shape) 
body_4.GetAssets().push_back(body_3_15_level) 

# Visualization shape 
body_3_16_shape = chrono.ChObjShapeFile() 
body_3_16_shape.SetFilename(shapes_dir +'body_3_16.obj') 
body_3_16_level = chrono.ChAssetLevel() 
body_3_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_16_level.GetAssets().push_back(body_3_16_shape) 
body_4.GetAssets().push_back(body_3_16_level) 

# Visualization shape 
body_3_17_shape = chrono.ChObjShapeFile() 
body_3_17_shape.SetFilename(shapes_dir +'body_3_17.obj') 
body_3_17_level = chrono.ChAssetLevel() 
body_3_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_17_level.GetAssets().push_back(body_3_17_shape) 
body_4.GetAssets().push_back(body_3_17_level) 

# Visualization shape 
body_3_18_shape = chrono.ChObjShapeFile() 
body_3_18_shape.SetFilename(shapes_dir +'body_3_18.obj') 
body_3_18_level = chrono.ChAssetLevel() 
body_3_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_18_level.GetAssets().push_back(body_3_18_shape) 
body_4.GetAssets().push_back(body_3_18_level) 

# Visualization shape 
body_3_19_shape = chrono.ChObjShapeFile() 
body_3_19_shape.SetFilename(shapes_dir +'body_3_19.obj') 
body_3_19_level = chrono.ChAssetLevel() 
body_3_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_19_level.GetAssets().push_back(body_3_19_shape) 
body_4.GetAssets().push_back(body_3_19_level) 

# Visualization shape 
body_3_20_shape = chrono.ChObjShapeFile() 
body_3_20_shape.SetFilename(shapes_dir +'body_3_20.obj') 
body_3_20_level = chrono.ChAssetLevel() 
body_3_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_20_level.GetAssets().push_back(body_3_20_shape) 
body_4.GetAssets().push_back(body_3_20_level) 

# Visualization shape 
body_3_21_shape = chrono.ChObjShapeFile() 
body_3_21_shape.SetFilename(shapes_dir +'body_3_21.obj') 
body_3_21_level = chrono.ChAssetLevel() 
body_3_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_21_level.GetAssets().push_back(body_3_21_shape) 
body_4.GetAssets().push_back(body_3_21_level) 

# Visualization shape 
body_3_22_shape = chrono.ChObjShapeFile() 
body_3_22_shape.SetFilename(shapes_dir +'body_3_22.obj') 
body_3_22_level = chrono.ChAssetLevel() 
body_3_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_22_level.GetAssets().push_back(body_3_22_shape) 
body_4.GetAssets().push_back(body_3_22_level) 

# Visualization shape 
body_3_23_shape = chrono.ChObjShapeFile() 
body_3_23_shape.SetFilename(shapes_dir +'body_3_23.obj') 
body_3_23_level = chrono.ChAssetLevel() 
body_3_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_23_level.GetAssets().push_back(body_3_23_shape) 
body_4.GetAssets().push_back(body_3_23_level) 

# Visualization shape 
body_3_24_shape = chrono.ChObjShapeFile() 
body_3_24_shape.SetFilename(shapes_dir +'body_3_24.obj') 
body_3_24_level = chrono.ChAssetLevel() 
body_3_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_24_level.GetAssets().push_back(body_3_24_shape) 
body_4.GetAssets().push_back(body_3_24_level) 

# Visualization shape 
body_3_25_shape = chrono.ChObjShapeFile() 
body_3_25_shape.SetFilename(shapes_dir +'body_3_25.obj') 
body_3_25_level = chrono.ChAssetLevel() 
body_3_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_25_level.GetAssets().push_back(body_3_25_shape) 
body_4.GetAssets().push_back(body_3_25_level) 

# Visualization shape 
body_3_26_shape = chrono.ChObjShapeFile() 
body_3_26_shape.SetFilename(shapes_dir +'body_3_26.obj') 
body_3_26_level = chrono.ChAssetLevel() 
body_3_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_26_level.GetAssets().push_back(body_3_26_shape) 
body_4.GetAssets().push_back(body_3_26_level) 

# Visualization shape 
body_3_27_shape = chrono.ChObjShapeFile() 
body_3_27_shape.SetFilename(shapes_dir +'body_3_27.obj') 
body_3_27_level = chrono.ChAssetLevel() 
body_3_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_27_level.GetAssets().push_back(body_3_27_shape) 
body_4.GetAssets().push_back(body_3_27_level) 

# Visualization shape 
body_3_28_shape = chrono.ChObjShapeFile() 
body_3_28_shape.SetFilename(shapes_dir +'body_3_28.obj') 
body_3_28_level = chrono.ChAssetLevel() 
body_3_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_28_level.GetAssets().push_back(body_3_28_shape) 
body_4.GetAssets().push_back(body_3_28_level) 

# Visualization shape 
body_3_29_shape = chrono.ChObjShapeFile() 
body_3_29_shape.SetFilename(shapes_dir +'body_3_29.obj') 
body_3_29_level = chrono.ChAssetLevel() 
body_3_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_29_level.GetAssets().push_back(body_3_29_shape) 
body_4.GetAssets().push_back(body_3_29_level) 

# Visualization shape 
body_3_30_shape = chrono.ChObjShapeFile() 
body_3_30_shape.SetFilename(shapes_dir +'body_3_30.obj') 
body_3_30_level = chrono.ChAssetLevel() 
body_3_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_30_level.GetAssets().push_back(body_3_30_shape) 
body_4.GetAssets().push_back(body_3_30_level) 

# Visualization shape 
body_3_31_shape = chrono.ChObjShapeFile() 
body_3_31_shape.SetFilename(shapes_dir +'body_3_31.obj') 
body_3_31_level = chrono.ChAssetLevel() 
body_3_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_31_level.GetAssets().push_back(body_3_31_shape) 
body_4.GetAssets().push_back(body_3_31_level) 

# Visualization shape 
body_3_32_shape = chrono.ChObjShapeFile() 
body_3_32_shape.SetFilename(shapes_dir +'body_3_32.obj') 
body_3_32_level = chrono.ChAssetLevel() 
body_3_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_32_level.GetAssets().push_back(body_3_32_shape) 
body_4.GetAssets().push_back(body_3_32_level) 

# Visualization shape 
body_3_33_shape = chrono.ChObjShapeFile() 
body_3_33_shape.SetFilename(shapes_dir +'body_3_33.obj') 
body_3_33_level = chrono.ChAssetLevel() 
body_3_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_33_level.GetAssets().push_back(body_3_33_shape) 
body_4.GetAssets().push_back(body_3_33_level) 

# Visualization shape 
body_3_34_shape = chrono.ChObjShapeFile() 
body_3_34_shape.SetFilename(shapes_dir +'body_3_34.obj') 
body_3_34_level = chrono.ChAssetLevel() 
body_3_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,0.02005)) 
body_3_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_3_34_level.GetAssets().push_back(body_3_34_shape) 
body_4.GetAssets().push_back(body_3_34_level) 

# Visualization shape 
body_3_35_shape = chrono.ChObjShapeFile() 
body_3_35_shape.SetFilename(shapes_dir +'body_3_35.obj') 
body_3_35_level = chrono.ChAssetLevel() 
body_3_35_level.GetFrame().SetPos(chrono.ChVectorD(0.0302,0.140000131576897,0.020050271710659)) 
body_3_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_3_35_level.GetAssets().push_back(body_3_35_shape) 
body_4.GetAssets().push_back(body_3_35_level) 

# Visualization shape 
body_3_36_shape = chrono.ChObjShapeFile() 
body_3_36_shape.SetFilename(shapes_dir +'body_3_36.obj') 
body_3_36_level = chrono.ChAssetLevel() 
body_3_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_36_level.GetAssets().push_back(body_3_36_shape) 
body_4.GetAssets().push_back(body_3_36_level) 

# Visualization shape 
body_3_37_shape = chrono.ChObjShapeFile() 
body_3_37_shape.SetFilename(shapes_dir +'body_3_37.obj') 
body_3_37_level = chrono.ChAssetLevel() 
body_3_37_level.GetFrame().SetPos(chrono.ChVectorD(0.01855,0.140000131576897,0.020050271710659)) 
body_3_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_3_37_level.GetAssets().push_back(body_3_37_shape) 
body_4.GetAssets().push_back(body_3_37_level) 

# Visualization shape 
body_3_38_shape = chrono.ChObjShapeFile() 
body_3_38_shape.SetFilename(shapes_dir +'body_3_38.obj') 
body_3_38_level = chrono.ChAssetLevel() 
body_3_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_38_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_38_level.GetAssets().push_back(body_3_38_shape) 
body_4.GetAssets().push_back(body_3_38_level) 

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('RH Shoulder.step-2')
body_5.SetPos(chrono.ChVectorD(-0.0504079632018997,0.085687859737262,0.21905208868513))
body_5.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_5.SetMass(0.118104660646891)
body_5.SetInertiaXX(chrono.ChVectorD(4.46841680139072e-05,0.000107948517541675,0.000120867442428233))
body_5.SetInertiaXY(chrono.ChVectorD(1.57611755382651e-05,1.1279955760135e-05,-2.22357650346175e-06))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0425217629672545,-0.0165393982541154,-0.0134769683159427),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.031,-0.029065938370768)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_2_shape = chrono.ChObjShapeFile() 
body_5_2_shape.SetFilename(shapes_dir +'body_5_2.obj') 
body_5_2_level = chrono.ChAssetLevel() 
body_5_2_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.014463319489083,-0.03174508818529)) 
body_5_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_2_level.GetAssets().push_back(body_5_2_shape) 
body_5.GetAssets().push_back(body_5_2_level) 

# Visualization shape 
body_5_3_shape = chrono.ChObjShapeFile() 
body_5_3_shape.SetFilename(shapes_dir +'body_5_3.obj') 
body_5_3_level = chrono.ChAssetLevel() 
body_5_3_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.04515,1.49991130626859E-13)) 
body_5_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,0.5,0.5,0.5)) 
body_5_3_level.GetAssets().push_back(body_5_3_shape) 
body_5.GetAssets().push_back(body_5_3_level) 

# Visualization shape 
body_5_4_shape = chrono.ChObjShapeFile() 
body_5_4_shape.SetFilename(shapes_dir +'body_5_4.obj') 
body_5_4_level = chrono.ChAssetLevel() 
body_5_4_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_4_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_4_level.GetAssets().push_back(body_5_4_shape) 
body_5.GetAssets().push_back(body_5_4_level) 

# Visualization shape 
body_5_5_shape = chrono.ChObjShapeFile() 
body_5_5_shape.SetFilename(shapes_dir +'body_5_5.obj') 
body_5_5_level = chrono.ChAssetLevel() 
body_5_5_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_5_level.GetAssets().push_back(body_5_5_shape) 
body_5.GetAssets().push_back(body_5_5_level) 

# Visualization shape 
body_5_6_shape = chrono.ChObjShapeFile() 
body_5_6_shape.SetFilename(shapes_dir +'body_5_6.obj') 
body_5_6_level = chrono.ChAssetLevel() 
body_5_6_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_6_level.GetAssets().push_back(body_5_6_shape) 
body_5.GetAssets().push_back(body_5_6_level) 

# Visualization shape 
body_5_7_shape = chrono.ChObjShapeFile() 
body_5_7_shape.SetFilename(shapes_dir +'body_5_7.obj') 
body_5_7_level = chrono.ChAssetLevel() 
body_5_7_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_7_level.GetAssets().push_back(body_5_7_shape) 
body_5.GetAssets().push_back(body_5_7_level) 

# Visualization shape 
body_5_8_shape = chrono.ChObjShapeFile() 
body_5_8_shape.SetFilename(shapes_dir +'body_5_8.obj') 
body_5_8_level = chrono.ChAssetLevel() 
body_5_8_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_8_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_8_level.GetAssets().push_back(body_5_8_shape) 
body_5.GetAssets().push_back(body_5_8_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845224,-0.0231,-0.0278499999998581)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_5.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_10_shape = chrono.ChObjShapeFile() 
body_5_10_shape.SetFilename(shapes_dir +'body_5_10.obj') 
body_5_10_level = chrono.ChAssetLevel() 
body_5_10_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_10_level.GetAssets().push_back(body_5_10_shape) 
body_5.GetAssets().push_back(body_5_10_level) 

# Visualization shape 
body_5_11_shape = chrono.ChObjShapeFile() 
body_5_11_shape.SetFilename(shapes_dir +'body_5_11.obj') 
body_5_11_level = chrono.ChAssetLevel() 
body_5_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_11_level.GetAssets().push_back(body_5_11_shape) 
body_5.GetAssets().push_back(body_5_11_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845224,-0.0231,-0.0278499999998588)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_5.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_13_shape = chrono.ChObjShapeFile() 
body_5_13_shape.SetFilename(shapes_dir +'body_5_13.obj') 
body_5_13_level = chrono.ChAssetLevel() 
body_5_13_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_13_level.GetAssets().push_back(body_5_13_shape) 
body_5.GetAssets().push_back(body_5_13_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845226,-0.0231,0.00755000000014186)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_5.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_15_shape = chrono.ChObjShapeFile() 
body_5_15_shape.SetFilename(shapes_dir +'body_5_15.obj') 
body_5_15_level = chrono.ChAssetLevel() 
body_5_15_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_15_level.GetAssets().push_back(body_5_15_shape) 
body_5.GetAssets().push_back(body_5_15_level) 

# Visualization shape 
body_5_16_shape = chrono.ChObjShapeFile() 
body_5_16_shape.SetFilename(shapes_dir +'body_5_16.obj') 
body_5_16_level = chrono.ChAssetLevel() 
body_5_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_16_level.GetAssets().push_back(body_5_16_shape) 
body_5.GetAssets().push_back(body_5_16_level) 

# Visualization shape 
body_5_17_shape = chrono.ChObjShapeFile() 
body_5_17_shape.SetFilename(shapes_dir +'body_5_17.obj') 
body_5_17_level = chrono.ChAssetLevel() 
body_5_17_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_17_level.GetAssets().push_back(body_5_17_shape) 
body_5.GetAssets().push_back(body_5_17_level) 

# Visualization shape 
body_5_18_shape = chrono.ChObjShapeFile() 
body_5_18_shape.SetFilename(shapes_dir +'body_5_18.obj') 
body_5_18_level = chrono.ChAssetLevel() 
body_5_18_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_18_level.GetAssets().push_back(body_5_18_shape) 
body_5.GetAssets().push_back(body_5_18_level) 

# Visualization shape 
body_5_19_shape = chrono.ChObjShapeFile() 
body_5_19_shape.SetFilename(shapes_dir +'body_5_19.obj') 
body_5_19_level = chrono.ChAssetLevel() 
body_5_19_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_19_level.GetAssets().push_back(body_5_19_shape) 
body_5.GetAssets().push_back(body_5_19_level) 

# Visualization shape 
body_5_20_shape = chrono.ChObjShapeFile() 
body_5_20_shape.SetFilename(shapes_dir +'body_5_20.obj') 
body_5_20_level = chrono.ChAssetLevel() 
body_5_20_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_20_level.GetAssets().push_back(body_5_20_shape) 
body_5.GetAssets().push_back(body_5_20_level) 

# Visualization shape 
body_5_21_shape = chrono.ChObjShapeFile() 
body_5_21_shape.SetFilename(shapes_dir +'body_5_21.obj') 
body_5_21_level = chrono.ChAssetLevel() 
body_5_21_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_21_level.GetAssets().push_back(body_5_21_shape) 
body_5.GetAssets().push_back(body_5_21_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845226,-0.0231,0.00755000000014115)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_5.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_23_shape = chrono.ChObjShapeFile() 
body_5_23_shape.SetFilename(shapes_dir +'body_5_23.obj') 
body_5_23_level = chrono.ChAssetLevel() 
body_5_23_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_23_level.GetAssets().push_back(body_5_23_shape) 
body_5.GetAssets().push_back(body_5_23_level) 

# Visualization shape 
body_5_24_shape = chrono.ChObjShapeFile() 
body_5_24_shape.SetFilename(shapes_dir +'body_5_24.obj') 
body_5_24_level = chrono.ChAssetLevel() 
body_5_24_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_24_level.GetAssets().push_back(body_5_24_shape) 
body_5.GetAssets().push_back(body_5_24_level) 

# Visualization shape 
body_5_25_shape = chrono.ChObjShapeFile() 
body_5_25_shape.SetFilename(shapes_dir +'body_5_25.obj') 
body_5_25_level = chrono.ChAssetLevel() 
body_5_25_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_25_level.GetAssets().push_back(body_5_25_shape) 
body_5.GetAssets().push_back(body_5_25_level) 

# Visualization shape 
body_5_26_shape = chrono.ChObjShapeFile() 
body_5_26_shape.SetFilename(shapes_dir +'body_5_26.obj') 
body_5_26_level = chrono.ChAssetLevel() 
body_5_26_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_26_level.GetAssets().push_back(body_5_26_shape) 
body_5.GetAssets().push_back(body_5_26_level) 

# Visualization shape 
body_5_27_shape = chrono.ChObjShapeFile() 
body_5_27_shape.SetFilename(shapes_dir +'body_5_27.obj') 
body_5_27_level = chrono.ChAssetLevel() 
body_5_27_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_27_level.GetAssets().push_back(body_5_27_shape) 
body_5.GetAssets().push_back(body_5_27_level) 

# Visualization shape 
body_5_28_shape = chrono.ChObjShapeFile() 
body_5_28_shape.SetFilename(shapes_dir +'body_5_28.obj') 
body_5_28_level = chrono.ChAssetLevel() 
body_5_28_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_28_level.GetAssets().push_back(body_5_28_shape) 
body_5.GetAssets().push_back(body_5_28_level) 

# Visualization shape 
body_5_29_shape = chrono.ChObjShapeFile() 
body_5_29_shape.SetFilename(shapes_dir +'body_5_29.obj') 
body_5_29_level = chrono.ChAssetLevel() 
body_5_29_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_29_level.GetAssets().push_back(body_5_29_shape) 
body_5.GetAssets().push_back(body_5_29_level) 

# Visualization shape 
body_5_30_shape = chrono.ChObjShapeFile() 
body_5_30_shape.SetFilename(shapes_dir +'body_5_30.obj') 
body_5_30_level = chrono.ChAssetLevel() 
body_5_30_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_30_level.GetAssets().push_back(body_5_30_shape) 
body_5.GetAssets().push_back(body_5_30_level) 

# Visualization shape 
body_5_31_shape = chrono.ChObjShapeFile() 
body_5_31_shape.SetFilename(shapes_dir +'body_5_31.obj') 
body_5_31_level = chrono.ChAssetLevel() 
body_5_31_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_31_level.GetAssets().push_back(body_5_31_shape) 
body_5.GetAssets().push_back(body_5_31_level) 

# Visualization shape 
body_5_32_shape = chrono.ChObjShapeFile() 
body_5_32_shape.SetFilename(shapes_dir +'body_5_32.obj') 
body_5_32_level = chrono.ChAssetLevel() 
body_5_32_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_32_level.GetAssets().push_back(body_5_32_shape) 
body_5.GetAssets().push_back(body_5_32_level) 

# Visualization shape 
body_5_33_shape = chrono.ChObjShapeFile() 
body_5_33_shape.SetFilename(shapes_dir +'body_5_33.obj') 
body_5_33_level = chrono.ChAssetLevel() 
body_5_33_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_33_level.GetAssets().push_back(body_5_33_shape) 
body_5.GetAssets().push_back(body_5_33_level) 

# Visualization shape 
body_5_34_shape = chrono.ChObjShapeFile() 
body_5_34_shape.SetFilename(shapes_dir +'body_5_34.obj') 
body_5_34_level = chrono.ChAssetLevel() 
body_5_34_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_34_level.GetAssets().push_back(body_5_34_shape) 
body_5.GetAssets().push_back(body_5_34_level) 

# Visualization shape 
body_5_35_shape = chrono.ChObjShapeFile() 
body_5_35_shape.SetFilename(shapes_dir +'body_5_35.obj') 
body_5_35_level = chrono.ChAssetLevel() 
body_5_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_35_level.GetAssets().push_back(body_5_35_shape) 
body_5.GetAssets().push_back(body_5_35_level) 

# Visualization shape 
body_5_36_shape = chrono.ChObjShapeFile() 
body_5_36_shape.SetFilename(shapes_dir +'body_5_36.obj') 
body_5_36_level = chrono.ChAssetLevel() 
body_5_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_36_level.GetAssets().push_back(body_5_36_shape) 
body_5.GetAssets().push_back(body_5_36_level) 

# Visualization shape 
body_5_37_shape = chrono.ChObjShapeFile() 
body_5_37_shape.SetFilename(shapes_dir +'body_5_37.obj') 
body_5_37_level = chrono.ChAssetLevel() 
body_5_37_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_37_level.GetAssets().push_back(body_5_37_shape) 
body_5.GetAssets().push_back(body_5_37_level) 

# Visualization shape 
body_5_38_shape = chrono.ChObjShapeFile() 
body_5_38_shape.SetFilename(shapes_dir +'body_5_38.obj') 
body_5_38_level = chrono.ChAssetLevel() 
body_5_38_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_38_level.GetAssets().push_back(body_5_38_shape) 
body_5.GetAssets().push_back(body_5_38_level) 

# Visualization shape 
body_5_39_shape = chrono.ChObjShapeFile() 
body_5_39_shape.SetFilename(shapes_dir +'body_5_39.obj') 
body_5_39_level = chrono.ChAssetLevel() 
body_5_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02955,-0.018,-0.00120000000000099)) 
body_5_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_39_level.GetAssets().push_back(body_5_39_shape) 
body_5.GetAssets().push_back(body_5_39_level) 

# Visualization shape 
body_5_40_shape = chrono.ChObjShapeFile() 
body_5_40_shape.SetFilename(shapes_dir +'body_5_40.obj') 
body_5_40_level = chrono.ChAssetLevel() 
body_5_40_level.GetFrame().SetPos(chrono.ChVectorD(-0.02955,-0.020820012245991,0.006918293207108)) 
body_5_40_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,0,-0.707106781186547)) 
body_5_40_level.GetAssets().push_back(body_5_40_shape) 
body_5.GetAssets().push_back(body_5_40_level) 

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.032,1.50005008414666E-13)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999997,0.500000000000003,0.499999999999997,0.500000000000003)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.014463319489083,-0.03174508818529)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_2_shape = chrono.ChObjShapeFile() 
body_5_2_shape.SetFilename(shapes_dir +'body_5_2.obj') 
body_5_2_level = chrono.ChAssetLevel() 
body_5_2_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.031,-0.029065938370768)) 
body_5_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_2_level.GetAssets().push_back(body_5_2_shape) 
body_5.GetAssets().push_back(body_5_2_level) 

# Visualization shape 
body_5_44_shape = chrono.ChObjShapeFile() 
body_5_44_shape.SetFilename(shapes_dir +'body_5_44.obj') 
body_5_44_level = chrono.ChAssetLevel() 
body_5_44_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,-0.018,-0.00120000000000099)) 
body_5_44_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186546,0,0,-0.707106781186549)) 
body_5_44_level.GetAssets().push_back(body_5_44_shape) 
body_5.GetAssets().push_back(body_5_44_level) 

# Visualization shape 
body_5_45_shape = chrono.ChObjShapeFile() 
body_5_45_shape.SetFilename(shapes_dir +'body_5_45.obj') 
body_5_45_level = chrono.ChAssetLevel() 
body_5_45_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_45_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_45_level.GetAssets().push_back(body_5_45_shape) 
body_5.GetAssets().push_back(body_5_45_level) 

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Upper Leg.step-1')
body_6.SetPos(chrono.ChVectorD(0.216874941702632,0.0866878597372726,0.485552088685123))
body_6.SetRot(chrono.ChQuaternionD(0.707106781186551,-0.707106781186544,-2.03001122407906e-15,2.80538289477362e-15))
body_6.SetMass(0.136105607367902)
body_6.SetInertiaXX(chrono.ChVectorD(0.000251122687518742,0.00027856514133726,4.31751690586657e-05))
body_6.SetInertiaXY(chrono.ChVectorD(1.42770165779724e-07,3.45711914254082e-06,-6.25406772913542e-06))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.000248284196117476,0.0632516253278484,0.0012090578668991),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999995,0.0072)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_6.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_6.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_6.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_6.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_6.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,0.00720000000000001)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.00055000000000005,-0.0071)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_6.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_6.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.0348499999999999,-0.0071)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_12_shape = chrono.ChObjShapeFile() 
body_6_12_shape.SetFilename(shapes_dir +'body_6_12.obj') 
body_6_12_level = chrono.ChAssetLevel() 
body_6_12_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_12_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_12_level.GetAssets().push_back(body_6_12_shape) 
body_6.GetAssets().push_back(body_6_12_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_6.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_6.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_6.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_6.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_6.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_6.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_6.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_6.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_6.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_6.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_6.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_6.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_6.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_6.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_6.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_6.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_6.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_6.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_6.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_6.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_6.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000084E-05)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_6.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.05897405927155,0.0039)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_6.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,0.01255)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-3.53553390593266E-16,3.53553390593276E-16,0.707106781186547)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_6.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,0.0039)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_6.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02055,0.00700000585427701,5.01644618990105E-05)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,-4.11384060427368E-30,0.707106781186548,4.8111017236421E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_6.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_39_shape = chrono.ChObjShapeFile() 
body_6_39_shape.SetFilename(shapes_dir +'body_6_39.obj') 
body_6_39_level = chrono.ChAssetLevel() 
body_6_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,0.14,-0.02)) 
body_6_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,3.53553390593269E-16,0.707106781186548,-3.53553390593269E-16)) 
body_6_39_level.GetAssets().push_back(body_6_39_shape) 
body_6.GetAssets().push_back(body_6_39_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.026097807647928,0.082122177814627,1.31942998193857E-10)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_6.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0.05897405927155,0.01255)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-3.53553390593266E-16,3.53553390593276E-16,0.707106781186547)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_6.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_42_shape = chrono.ChObjShapeFile() 
body_6_42_shape.SetFilename(shapes_dir +'body_6_42.obj') 
body_6_42_level = chrono.ChAssetLevel() 
body_6_42_level.GetFrame().SetPos(chrono.ChVectorD(0.02555,0.14,-0.02)) 
body_6_42_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186551,1.00152230238239E-30,-8.51800585778293E-30,-0.707106781186543)) 
body_6_42_level.GetAssets().push_back(body_6_42_shape) 
body_6.GetAssets().push_back(body_6_42_level) 

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(0.0332000000000001,0.00700000585427696,5.01644618990105E-05)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,-4.11384060427368E-30,0.707106781186548,4.8111017236421E-30)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_6.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_6_44_shape = chrono.ChObjShapeFile() 
body_6_44_shape.SetFilename(shapes_dir +'body_6_44.obj') 
body_6_44_level = chrono.ChAssetLevel() 
body_6_44_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_44_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_44_level.GetAssets().push_back(body_6_44_shape) 
body_6.GetAssets().push_back(body_6_44_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.017347807647928,0.0821221778146269,1.31942998193857E-10)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,-3.53553390593279E-16,-0.707106781186548,-3.53553390593278E-16)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_6.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_46_shape = chrono.ChObjShapeFile() 
body_6_46_shape.SetFilename(shapes_dir +'body_6_46.obj') 
body_6_46_level = chrono.ChAssetLevel() 
body_6_46_level.GetFrame().SetPos(chrono.ChVectorD(-0.02655,0.14811829320711,-0.022820012245991)) 
body_6_46_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,-0.5,0.5)) 
body_6_46_level.GetAssets().push_back(body_6_46_shape) 
body_6.GetAssets().push_back(body_6_46_level) 

# Visualization shape 
body_6_47_shape = chrono.ChObjShapeFile() 
body_6_47_shape.SetFilename(shapes_dir +'body_6_47.obj') 
body_6_47_level = chrono.ChAssetLevel() 
body_6_47_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_47_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_47_level.GetAssets().push_back(body_6_47_shape) 
body_6.GetAssets().push_back(body_6_47_level) 

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('LH Shoulder.step-3')
body_7.SetPos(chrono.ChVectorD(0.216874941702632,0.0856878597372402,0.225052088685129))
body_7.SetRot(chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,1.18304262385918e-13,-1.18289044981994e-13))
body_7.SetMass(0.118103187382885)
body_7.SetInertiaXX(chrono.ChVectorD(4.468307807592e-05,0.000107946537422069,0.000120866016341517))
body_7.SetInertiaXY(chrono.ChVectorD(1.57606503508102e-05,1.12790186398425e-05,-2.22311335800558e-06))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0425214406592162,-0.0165396904773734,0.0134771264279906),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.04515,-1.50005008414666E-13)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,-0.5,0.5)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_7.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.031,0.029065938370768)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-1.60152163354934E-31,0.707106781186547,1.18752284392434E-31)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_7.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.032,-1.50005008414666E-13)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999997,-0.500000000000003,-0.499999999999997,0.500000000000003)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_7.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.014463319489083,0.03174508818529)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-1.60152163354934E-31,0.707106781186547,1.18752284392434E-31)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_7.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845226,-0.0231,-0.00755000000014316)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,-0.500000000000005,0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_7.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_7.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_7.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_7.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_7.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_7.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845234,-0.0231,0.0278499999998568)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,-0.500000000000005,0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_7.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845227,-0.0231,-0.00755000000014286)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,-0.500000000000005,0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_7.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_7.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_7.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845234,-0.0231,0.0278499999998571)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,-0.500000000000005,0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_7.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_7_16_shape = chrono.ChObjShapeFile() 
body_7_16_shape.SetFilename(shapes_dir +'body_7_16.obj') 
body_7_16_level = chrono.ChAssetLevel() 
body_7_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_7_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_7_16_level.GetAssets().push_back(body_7_16_shape) 
body_7.GetAssets().push_back(body_7_16_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_7.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_7.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_7.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_7.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_7.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_7.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_7.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_7.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_7.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_7.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_7.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_7.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_7.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_7.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_7.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_7.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_7.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_7.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_7.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_7.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_7.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_7.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_7_39_shape = chrono.ChObjShapeFile() 
body_7_39_shape.SetFilename(shapes_dir +'body_7_39.obj') 
body_7_39_level = chrono.ChAssetLevel() 
body_7_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_39_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_39_level.GetAssets().push_back(body_7_39_shape) 
body_7.GetAssets().push_back(body_7_39_level) 

# Visualization shape 
body_7_40_shape = chrono.ChObjShapeFile() 
body_7_40_shape.SetFilename(shapes_dir +'body_7_40.obj') 
body_7_40_level = chrono.ChAssetLevel() 
body_7_40_level.GetFrame().SetPos(chrono.ChVectorD(-0.02955,-0.020820012245991,-0.006918293207108)) 
body_7_40_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,1.65260765732165E-31,-1.13643682015203E-31,-0.707106781186547)) 
body_7_40_level.GetAssets().push_back(body_7_40_shape) 
body_7.GetAssets().push_back(body_7_40_level) 

# Visualization shape 
body_6_39_shape = chrono.ChObjShapeFile() 
body_6_39_shape.SetFilename(shapes_dir +'body_6_39.obj') 
body_6_39_level = chrono.ChAssetLevel() 
body_6_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02955,-0.018,0.00120000000000101)) 
body_6_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-1.60152163354934E-31,0.707106781186547,1.18752284392434E-31)) 
body_6_39_level.GetAssets().push_back(body_6_39_shape) 
body_7.GetAssets().push_back(body_6_39_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.014463319489083,0.03174508818529)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-1.60152163354934E-31,0.707106781186547,1.18752284392434E-31)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_7.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.031,0.029065938370768)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-1.60152163354934E-31,0.707106781186547,1.18752284392434E-31)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_7.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_7_44_shape = chrono.ChObjShapeFile() 
body_7_44_shape.SetFilename(shapes_dir +'body_7_44.obj') 
body_7_44_level = chrono.ChAssetLevel() 
body_7_44_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,-0.018,0.00120000000000101)) 
body_7_44_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186546,-3.43247411445268E-30,-1.13643682015203E-31,-0.707106781186549)) 
body_7_44_level.GetAssets().push_back(body_7_44_shape) 
body_7.GetAssets().push_back(body_7_44_level) 

# Visualization shape 
body_7_45_shape = chrono.ChObjShapeFile() 
body_7_45_shape.SetFilename(shapes_dir +'body_7_45.obj') 
body_7_45_level = chrono.ChAssetLevel() 
body_7_45_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_45_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_45_level.GetAssets().push_back(body_7_45_shape) 
body_7.GetAssets().push_back(body_7_45_level) 

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('Lower Leg.step-3')
body_8.SetPos(chrono.ChVectorD(0.216874941702632,0.0868878597372414,0.250052088685129))
body_8.SetRot(chrono.ChQuaternionD(0.707106781186551,-0.707106781186544,1.18228211032449e-13,-1.18212993628527e-13))
body_8.SetMass(0.0965195912663027)
body_8.SetInertiaXX(chrono.ChVectorD(0.000185078635413759,0.000191942424654835,1.37684925494404e-05))
body_8.SetInertiaXY(chrono.ChVectorD(8.37154460668766e-09,-1.85165490757606e-06,-5.63860607834651e-07))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000646606827372261,0.0946701125929855,-0.0216225845247406),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_8.GetAssets().push_back(body_8_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,-0.0272)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_8.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_8.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_8.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_8.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_8.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_8.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,-0.0272)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_8.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,-0.0129)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_8.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_8.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_8.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,-0.0129)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_8.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_8_13_shape = chrono.ChObjShapeFile() 
body_8_13_shape.SetFilename(shapes_dir +'body_8_13.obj') 
body_8_13_level = chrono.ChAssetLevel() 
body_8_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_8_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_8_13_level.GetAssets().push_back(body_8_13_shape) 
body_8.GetAssets().push_back(body_8_13_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_8.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_8.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_8.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_8.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_8.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_8.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_8.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_8.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_8.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_8.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_8.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_8.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_8.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_8.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_8.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_8.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_8.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_8.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_8.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_8.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_8.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,0.5)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_8.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.01855,0.140000131576897,-0.020050271710659)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.74328671651513E-30,0.707106781186547,2.83480223843223E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_8.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(0.0302,0.140000131576897,-0.020050271710659)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-2.74328671651513E-30,0.707106781186547,2.83480223843223E-30)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_8.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_8_38_shape = chrono.ChObjShapeFile() 
body_8_38_shape.SetFilename(shapes_dir +'body_8_38.obj') 
body_8_38_level = chrono.ChAssetLevel() 
body_8_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_38_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_38_level.GetAssets().push_back(body_8_38_shape) 
body_8.GetAssets().push_back(body_8_38_level) 

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Torso.step-1')
body_9.SetPos(chrono.ChVectorD(0.0832334892503638,0.0704824589092791,0.303052088685129))
body_9.SetRot(chrono.ChQuaternionD(-2.46885013108226e-15,-2.46885013108227e-15,0.707106781186549,0.707106781186546))
body_9.SetMass(1.03046354336496)
body_9.SetInertiaXX(chrono.ChVectorD(0.00880767150025151,0.0109619853835292,0.00357622293662154))
body_9.SetInertiaXY(chrono.ChVectorD(2.01727243139256e-05,-3.1905239361894e-05,0.000145525724381463))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00104603044672423,-0.00439559841400526,0.0310139016884599),chrono.ChQuaternionD(1,0,0,0)))
body_9.SetBodyFixed(True)

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.080060730784165,-0.144650000000001,0.032499851288557)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.080060730784166,-0.144650000000001,0.032499851288557)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_9_3_shape = chrono.ChObjShapeFile() 
body_9_3_shape.SetFilename(shapes_dir +'body_9_3.obj') 
body_9_3_level = chrono.ChAssetLevel() 
body_9_3_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_3_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_3_level.GetAssets().push_back(body_9_3_shape) 
body_9.GetAssets().push_back(body_9_3_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.033435049097141,0.00868078199699301,0.010000000050555)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_5_shape = chrono.ChObjShapeFile() 
body_9_5_shape.SetFilename(shapes_dir +'body_9_5.obj') 
body_9_5_level = chrono.ChAssetLevel() 
body_9_5_level.GetFrame().SetPos(chrono.ChVectorD(0.03898,-0.119000000000001,0.0457499999999998)) 
body_9_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_5_level.GetAssets().push_back(body_9_5_shape) 
body_9.GetAssets().push_back(body_9_5_level) 

# Visualization shape 
body_9_6_shape = chrono.ChObjShapeFile() 
body_9_6_shape.SetFilename(shapes_dir +'body_9_6.obj') 
body_9_6_level = chrono.ChAssetLevel() 
body_9_6_level.GetFrame().SetPos(chrono.ChVectorD(0.04,-0.131050000000001,0.0459999999999999)) 
body_9_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.25280609221184,4.29650775268414E-16,0.967516966125441,-5.91271212405635E-16)) 
body_9_6_level.GetAssets().push_back(body_9_6_shape) 
body_9.GetAssets().push_back(body_9_6_level) 

# Visualization shape 
body_9_7_shape = chrono.ChObjShapeFile() 
body_9_7_shape.SetFilename(shapes_dir +'body_9_7.obj') 
body_9_7_level = chrono.ChAssetLevel() 
body_9_7_level.GetFrame().SetPos(chrono.ChVectorD(0.0405,-0.131199999698941,0.0459999999999999)) 
body_9_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186549,0.707106781186546,-4.95433823295186E-46,0)) 
body_9_7_level.GetAssets().push_back(body_9_7_shape) 
body_9.GetAssets().push_back(body_9_7_level) 

# Visualization shape 
body_9_8_shape = chrono.ChObjShapeFile() 
body_9_8_shape.SetFilename(shapes_dir +'body_9_8.obj') 
body_9_8_level = chrono.ChAssetLevel() 
body_9_8_level.GetFrame().SetPos(chrono.ChVectorD(0.04202,-0.131000000000001,0.0457499999999999)) 
body_9_8_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_8_level.GetAssets().push_back(body_9_8_shape) 
body_9.GetAssets().push_back(body_9_8_level) 

# Visualization shape 
body_9_9_shape = chrono.ChObjShapeFile() 
body_9_9_shape.SetFilename(shapes_dir +'body_9_9.obj') 
body_9_9_level = chrono.ChAssetLevel() 
body_9_9_level.GetFrame().SetPos(chrono.ChVectorD(0.04152,-0.131050000000001,0.0460499999999999)) 
body_9_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-1.06066017177982E-15,-3.53553390593272E-16,0.707106781186548,-0.707106781186547)) 
body_9_9_level.GetAssets().push_back(body_9_9_shape) 
body_9.GetAssets().push_back(body_9_9_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.075202230277936,0.018340754885703,0.04475)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.040582598970716,0.008493616816591,0.010000000050556)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.034848604305766,0.062662277545673,0.010000000050555)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.07605298109793,0.050829617947409,0.01225)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148594,0.707046201633167,-0.00925574179148524,0.707046201633167)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_8_shape = chrono.ChObjShapeFile() 
body_9_8_shape.SetFilename(shapes_dir +'body_9_8.obj') 
body_9_8_level = chrono.ChAssetLevel() 
body_9_8_level.GetFrame().SetPos(chrono.ChVectorD(0.05002,-0.131000000000001,0.0457499999999999)) 
body_9_8_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_8_level.GetAssets().push_back(body_9_8_shape) 
body_9.GetAssets().push_back(body_9_8_level) 

# Visualization shape 
body_9_7_shape = chrono.ChObjShapeFile() 
body_9_7_shape.SetFilename(shapes_dir +'body_9_7.obj') 
body_9_7_level = chrono.ChAssetLevel() 
body_9_7_level.GetFrame().SetPos(chrono.ChVectorD(0.0485,-0.131199999698941,0.0459999999999999)) 
body_9_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186549,0.707106781186546,-4.95433823295186E-46,0)) 
body_9_7_level.GetAssets().push_back(body_9_7_shape) 
body_9.GetAssets().push_back(body_9_7_level) 

# Visualization shape 
body_9_9_shape = chrono.ChObjShapeFile() 
body_9_9_shape.SetFilename(shapes_dir +'body_9_9.obj') 
body_9_9_level = chrono.ChAssetLevel() 
body_9_9_level.GetFrame().SetPos(chrono.ChVectorD(0.04952,-0.131050000000001,0.0460499999999999)) 
body_9_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-1.06066017177982E-15,-3.53553390593272E-16,0.707106781186548,-0.707106781186547)) 
body_9_9_level.GetAssets().push_back(body_9_9_shape) 
body_9.GetAssets().push_back(body_9_9_level) 

# Visualization shape 
body_9_5_shape = chrono.ChObjShapeFile() 
body_9_5_shape.SetFilename(shapes_dir +'body_9_5.obj') 
body_9_5_level = chrono.ChAssetLevel() 
body_9_5_level.GetFrame().SetPos(chrono.ChVectorD(0.04698,-0.119000000000001,0.0457499999999998)) 
body_9_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_5_level.GetAssets().push_back(body_9_5_shape) 
body_9.GetAssets().push_back(body_9_5_level) 

# Visualization shape 
body_9_6_shape = chrono.ChObjShapeFile() 
body_9_6_shape.SetFilename(shapes_dir +'body_9_6.obj') 
body_9_6_level = chrono.ChAssetLevel() 
body_9_6_level.GetFrame().SetPos(chrono.ChVectorD(0.048,-0.131050000000001,0.0459999999999999)) 
body_9_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.25280609221184,4.29650775268414E-16,0.967516966125441,-5.91271212405635E-16)) 
body_9_6_level.GetAssets().push_back(body_9_6_shape) 
body_9.GetAssets().push_back(body_9_6_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.041996154179341,0.062475112365271,0.010000000050556)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_9_20_shape = chrono.ChObjShapeFile() 
body_9_20_shape.SetFilename(shapes_dir +'body_9_20.obj') 
body_9_20_level = chrono.ChAssetLevel() 
body_9_20_level.GetFrame().SetPos(chrono.ChVectorD(0,0.0988000000000001,0.03701)) 
body_9_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.500000000000001)) 
body_9_20_level.GetAssets().push_back(body_9_20_shape) 
body_9.GetAssets().push_back(body_9_20_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.079416091564366,-0.107250000000001,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.081216373672247,-0.0385,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.0434,0.123,0.0404)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.08532756335861,0.1185,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.081216373672247,-0.0385,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.079416091564366,-0.10725,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.039608,-0.049,0.00599999999999999)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.030812453615829,-0.049,0.0465)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.08532756335861,0.1185,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.03081245361583,-0.049,0.0465)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.039608,-0.049,0.00599999999999999)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.080060730784165,-0.136000000000001,0.032499851288556)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.039608,-0.03785,0.00599999999999999)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.030812453615829,-0.03785,0.0465)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.0434,0.123,0.00699999999999999)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.080060730784166,-0.136000000000001,0.032499851288557)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.0434,0.123,0.00700000000000001)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0434,0.113849999999999,0.00699999999999999)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.085327563358609,0.1185,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_9_40_shape = chrono.ChObjShapeFile() 
body_9_40_shape.SetFilename(shapes_dir +'body_9_40.obj') 
body_9_40_level = chrono.ChAssetLevel() 
body_9_40_level.GetFrame().SetPos(chrono.ChVectorD(0.052523704025348,0.0977500000000001,0.00220000000000001)) 
body_9_40_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_40_level.GetAssets().push_back(body_9_40_shape) 
body_9.GetAssets().push_back(body_9_40_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.079416091564366,-0.10725,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.079416091564366,-0.107250000000001,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.0434,0.123,0.0404)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.085327563358609,0.1185,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.081216373672247,-0.0385,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0434,0.113849999999999,0.0404)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.0434,0.113849999999999,0.0404)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.03081245361583,-0.03785,0.0465)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_9_49_shape = chrono.ChObjShapeFile() 
body_9_49_shape.SetFilename(shapes_dir +'body_9_49.obj') 
body_9_49_level = chrono.ChAssetLevel() 
body_9_49_level.GetFrame().SetPos(chrono.ChVectorD(-0.0335,-0.129500000000001,0.014)) 
body_9_49_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_49_level.GetAssets().push_back(body_9_49_shape) 
body_9.GetAssets().push_back(body_9_49_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.081216373672247,-0.0385,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.0434,0.113849999999999,0.00699999999999999)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.039608,-0.03785,0.00599999999999999)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_9.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_9_53_shape = chrono.ChObjShapeFile() 
body_9_53_shape.SetFilename(shapes_dir +'body_9_53.obj') 
body_9_53_level = chrono.ChAssetLevel() 
body_9_53_level.GetFrame().SetPos(chrono.ChVectorD(-0.0335,-0.129500000000001,0.03)) 
body_9_53_level.GetFrame().SetRot(chrono.ChQuaternionD(0.683012701892219,0.683012701892219,0.183012701892219,-0.183012701892219)) 
body_9_53_level.GetAssets().push_back(body_9_53_shape) 
body_9.GetAssets().push_back(body_9_53_level) 

# Visualization shape 
body_9_54_shape = chrono.ChObjShapeFile() 
body_9_54_shape.SetFilename(shapes_dir +'body_9_54.obj') 
body_9_54_level = chrono.ChAssetLevel() 
body_9_54_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_54_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_54_level.GetAssets().push_back(body_9_54_shape) 
body_9.GetAssets().push_back(body_9_54_level) 

# Visualization shape 
body_9_55_shape = chrono.ChObjShapeFile() 
body_9_55_shape.SetFilename(shapes_dir +'body_9_55.obj') 
body_9_55_level = chrono.ChAssetLevel() 
body_9_55_level.GetFrame().SetPos(chrono.ChVectorD(0.0235,-0.118500000000001,0.05)) 
body_9_55_level.GetFrame().SetRot(chrono.ChQuaternionD(0.49999999999997,0.50000000000003,-0.500000000000031,-0.49999999999997)) 
body_9_55_level.GetAssets().push_back(body_9_55_shape) 
body_9.GetAssets().push_back(body_9_55_level) 

# Visualization shape 
body_9_56_shape = chrono.ChObjShapeFile() 
body_9_56_shape.SetFilename(shapes_dir +'body_9_56.obj') 
body_9_56_level = chrono.ChAssetLevel() 
body_9_56_level.GetFrame().SetPos(chrono.ChVectorD(-0.0292,-0.127500000000001,0.0495)) 
body_9_56_level.GetFrame().SetRot(chrono.ChQuaternionD(0,1,0,1E-15)) 
body_9_56_level.GetAssets().push_back(body_9_56_shape) 
body_9.GetAssets().push_back(body_9_56_level) 

# Visualization shape 
body_9_57_shape = chrono.ChObjShapeFile() 
body_9_57_shape.SetFilename(shapes_dir +'body_9_57.obj') 
body_9_57_level = chrono.ChAssetLevel() 
body_9_57_level.GetFrame().SetPos(chrono.ChVectorD(0.084624521612707,0.034349593881785,0.0285)) 
body_9_57_level.GetFrame().SetRot(chrono.ChQuaternionD(0.506501961572675,0.506501961572675,0.493412366001332,0.493412366001332)) 
body_9_57_level.GetAssets().push_back(body_9_57_shape) 
body_9.GetAssets().push_back(body_9_57_level) 

# Visualization shape 
body_9_58_shape = chrono.ChObjShapeFile() 
body_9_58_shape.SetFilename(shapes_dir +'body_9_58.obj') 
body_9_58_level = chrono.ChAssetLevel() 
body_9_58_level.GetFrame().SetPos(chrono.ChVectorD(-0.0105,0.00110000000000005,0.039)) 
body_9_58_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.500000000000001,0.5,0.499999999999999)) 
body_9_58_level.GetAssets().push_back(body_9_58_shape) 
body_9.GetAssets().push_back(body_9_58_level) 

# Visualization shape 
body_9_59_shape = chrono.ChObjShapeFile() 
body_9_59_shape.SetFilename(shapes_dir +'body_9_59.obj') 
body_9_59_level = chrono.ChAssetLevel() 
body_9_59_level.GetFrame().SetPos(chrono.ChVectorD(-0.0352177394552567,0.0156365001545289,0.033190000050556)) 
body_9_59_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_59_level.GetAssets().push_back(body_9_59_shape) 
body_9.GetAssets().push_back(body_9_59_level) 

# Visualization shape 
body_9_60_shape = chrono.ChObjShapeFile() 
body_9_60_shape.SetFilename(shapes_dir +'body_9_60.obj') 
body_9_60_level = chrono.ChAssetLevel() 
body_9_60_level.GetFrame().SetPos(chrono.ChVectorD(-0.0456821601755066,0.00841009724646996,0.022507500050556)) 
body_9_60_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_60_level.GetAssets().push_back(body_9_60_shape) 
body_9.GetAssets().push_back(body_9_60_level) 

# Visualization shape 
body_9_61_shape = chrono.ChObjShapeFile() 
body_9_61_shape.SetFilename(shapes_dir +'body_9_61.obj') 
body_9_61_level = chrono.ChAssetLevel() 
body_9_61_level.GetFrame().SetPos(chrono.ChVectorD(-0.0477600056703814,0.0113567153247809,0.033252500050556)) 
body_9_61_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_61_level.GetAssets().push_back(body_9_61_shape) 
body_9.GetAssets().push_back(body_9_61_level) 

# Visualization shape 
body_9_60_shape = chrono.ChObjShapeFile() 
body_9_60_shape.SetFilename(shapes_dir +'body_9_60.obj') 
body_9_60_level = chrono.ChAssetLevel() 
body_9_60_level.GetFrame().SetPos(chrono.ChVectorD(-0.0456821601755066,0.00841009724646991,0.030252500050556)) 
body_9_60_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_60_level.GetAssets().push_back(body_9_60_shape) 
body_9.GetAssets().push_back(body_9_60_level) 

# Visualization shape 
body_9_63_shape = chrono.ChObjShapeFile() 
body_9_63_shape.SetFilename(shapes_dir +'body_9_63.obj') 
body_9_63_level = chrono.ChAssetLevel() 
body_9_63_level.GetFrame().SetPos(chrono.ChVectorD(-0.0388572512344134,0.0056378025388702,0.029380000050556)) 
body_9_63_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_63_level.GetAssets().push_back(body_9_63_shape) 
body_9.GetAssets().push_back(body_9_63_level) 

# Visualization shape 
body_9_61_shape = chrono.ChObjShapeFile() 
body_9_61_shape.SetFilename(shapes_dir +'body_9_61.obj') 
body_9_61_level = chrono.ChAssetLevel() 
body_9_61_level.GetFrame().SetPos(chrono.ChVectorD(-0.0477600056703814,0.0113567153247808,0.025507500050556)) 
body_9_61_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_61_level.GetAssets().push_back(body_9_61_shape) 
body_9.GetAssets().push_back(body_9_61_level) 

# Visualization shape 
body_9_59_shape = chrono.ChObjShapeFile() 
body_9_59_shape.SetFilename(shapes_dir +'body_9_59.obj') 
body_9_59_level = chrono.ChAssetLevel() 
body_9_59_level.GetFrame().SetPos(chrono.ChVectorD(-0.0352177394552566,0.0156365001545289,0.025570000050556)) 
body_9_59_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001331,0.506501961572676,-0.493412366001331,0.506501961572676)) 
body_9_59_level.GetAssets().push_back(body_9_59_shape) 
body_9.GetAssets().push_back(body_9_59_level) 

# Visualization shape 
body_9_66_shape = chrono.ChObjShapeFile() 
body_9_66_shape.SetFilename(shapes_dir +'body_9_66.obj') 
body_9_66_level = chrono.ChAssetLevel() 
body_9_66_level.GetFrame().SetPos(chrono.ChVectorD(-0.041864982624243,0.120498430295766,0.026500000139963)) 
body_9_66_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_66_level.GetAssets().push_back(body_9_66_shape) 
body_9.GetAssets().push_back(body_9_66_level) 

# Visualization shape 
body_9_67_shape = chrono.ChObjShapeFile() 
body_9_67_shape.SetFilename(shapes_dir +'body_9_67.obj') 
body_9_67_level = chrono.ChAssetLevel() 
body_9_67_level.GetFrame().SetPos(chrono.ChVectorD(-0.0408051202215457,0.0655073290645491,0.039235000050556)) 
body_9_67_level.GetFrame().SetRot(chrono.ChQuaternionD(0.009255741791487,0.707046201633167,0.009255741791487,-0.707046201633167)) 
body_9_67_level.GetAssets().push_back(body_9_67_shape) 
body_9.GetAssets().push_back(body_9_67_level) 

# Visualization shape 
body_9_68_shape = chrono.ChObjShapeFile() 
body_9_68_shape.SetFilename(shapes_dir +'body_9_68.obj') 
body_9_68_level = chrono.ChAssetLevel() 
body_9_68_level.GetFrame().SetPos(chrono.ChVectorD(-0.0412890897614698,0.0985059691463034,0.041500000139963)) 
body_9_68_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_68_level.GetAssets().push_back(body_9_68_shape) 
body_9.GetAssets().push_back(body_9_68_level) 

# Visualization shape 
body_9_69_shape = chrono.ChObjShapeFile() 
body_9_69_shape.SetFilename(shapes_dir +'body_9_69.obj') 
body_9_69_level = chrono.ChAssetLevel() 
body_9_69_level.GetFrame().SetPos(chrono.ChVectorD(-0.0456198641752418,0.0728838215006834,0.017000000050556)) 
body_9_69_level.GetFrame().SetRot(chrono.ChQuaternionD(0.716301943424654,3.01135793015002E-32,-1.37662076806858E-31,-0.69779045984168)) 
body_9_69_level.GetAssets().push_back(body_9_69_shape) 
body_9.GetAssets().push_back(body_9_69_level) 

# Visualization shape 
body_9_61_shape = chrono.ChObjShapeFile() 
body_9_61_shape.SetFilename(shapes_dir +'body_9_61.obj') 
body_9_61_level = chrono.ChAssetLevel() 
body_9_61_level.GetFrame().SetPos(chrono.ChVectorD(-0.0490138814943285,0.05924030119111,0.027252500050556)) 
body_9_61_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_61_level.GetAssets().push_back(body_9_61_shape) 
body_9.GetAssets().push_back(body_9_61_level) 

# Visualization shape 
body_9_61_shape = chrono.ChObjShapeFile() 
body_9_61_shape.SetFilename(shapes_dir +'body_9_61.obj') 
body_9_61_level = chrono.ChAssetLevel() 
body_9_61_level.GetFrame().SetPos(chrono.ChVectorD(-0.0490138814943285,0.05924030119111,0.019507500050556)) 
body_9_61_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_61_level.GetAssets().push_back(body_9_61_shape) 
body_9.GetAssets().push_back(body_9_61_level) 

# Visualization shape 
body_9_63_shape = chrono.ChObjShapeFile() 
body_9_63_shape.SetFilename(shapes_dir +'body_9_63.obj') 
body_9_63_level = chrono.ChAssetLevel() 
body_9_63_level.GetFrame().SetPos(chrono.ChVectorD(-0.0404226327432242,0.0654173105724085,0.023380000050556)) 
body_9_63_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_63_level.GetAssets().push_back(body_9_63_shape) 
body_9.GetAssets().push_back(body_9_63_level) 

# Visualization shape 
body_9_59_shape = chrono.ChObjShapeFile() 
body_9_59_shape.SetFilename(shapes_dir +'body_9_59.obj') 
body_9_59_level = chrono.ChAssetLevel() 
body_9_59_level.GetFrame().SetPos(chrono.ChVectorD(-0.0362648173875716,0.0556227931535511,0.027190000050556)) 
body_9_59_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_59_level.GetAssets().push_back(body_9_59_shape) 
body_9.GetAssets().push_back(body_9_59_level) 

# Visualization shape 
body_9_60_shape = chrono.ChObjShapeFile() 
body_9_60_shape.SetFilename(shapes_dir +'body_9_60.obj') 
body_9_60_level = chrono.ChAssetLevel() 
body_9_60_level.GetFrame().SetPos(chrono.ChVectorD(-0.047093097689301,0.0622916270626525,0.022507500050556)) 
body_9_60_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_60_level.GetAssets().push_back(body_9_60_shape) 
body_9.GetAssets().push_back(body_9_60_level) 

# Visualization shape 
body_9_60_shape = chrono.ChObjShapeFile() 
body_9_60_shape.SetFilename(shapes_dir +'body_9_60.obj') 
body_9_60_level = chrono.ChAssetLevel() 
body_9_60_level.GetFrame().SetPos(chrono.ChVectorD(-0.047093097689301,0.0622916270626524,0.030252500050556)) 
body_9_60_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_60_level.GetAssets().push_back(body_9_60_shape) 
body_9.GetAssets().push_back(body_9_60_level) 

# Visualization shape 
body_9_59_shape = chrono.ChObjShapeFile() 
body_9_59_shape.SetFilename(shapes_dir +'body_9_59.obj') 
body_9_59_level = chrono.ChAssetLevel() 
body_9_59_level.GetFrame().SetPos(chrono.ChVectorD(-0.0362648173875716,0.0556227931535512,0.019570000050556)) 
body_9_59_level.GetFrame().SetRot(chrono.ChQuaternionD(0.493412366001332,-0.506501961572675,0.493412366001331,0.506501961572676)) 
body_9_59_level.GetAssets().push_back(body_9_59_shape) 
body_9.GetAssets().push_back(body_9_59_level) 

# Visualization shape 
body_9_77_shape = chrono.ChObjShapeFile() 
body_9_77_shape.SetFilename(shapes_dir +'body_9_77.obj') 
body_9_77_level = chrono.ChAssetLevel() 
body_9_77_level.GetFrame().SetPos(chrono.ChVectorD(-0.0390509606518917,0.0130352667436893,0.046000000050556)) 
body_9_77_level.GetFrame().SetRot(chrono.ChQuaternionD(0.69779045984168,-3.09124538361145E-32,1.41314074679381E-31,0.716301943424654)) 
body_9_77_level.GetAssets().push_back(body_9_77_shape) 
body_9.GetAssets().push_back(body_9_77_level) 

# Visualization shape 
body_9_78_shape = chrono.ChObjShapeFile() 
body_9_78_shape.SetFilename(shapes_dir +'body_9_78.obj') 
body_9_78_level = chrono.ChAssetLevel() 
body_9_78_level.GetFrame().SetPos(chrono.ChVectorD(-0.040425250438055,0.0655172763049061,0.007000000050556)) 
body_9_78_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_78_level.GetAssets().push_back(body_9_78_shape) 
body_9.GetAssets().push_back(body_9_78_level) 

# Visualization shape 
body_9_79_shape = chrono.ChObjShapeFile() 
body_9_79_shape.SetFilename(shapes_dir +'body_9_79.obj') 
body_9_79_level = chrono.ChAssetLevel() 
body_9_79_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_79_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_79_level.GetAssets().push_back(body_9_79_shape) 
body_9.GetAssets().push_back(body_9_79_level) 

# Visualization shape 
body_9_80_shape = chrono.ChObjShapeFile() 
body_9_80_shape.SetFilename(shapes_dir +'body_9_80.obj') 
body_9_80_level = chrono.ChAssetLevel() 
body_9_80_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_80_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_80_level.GetAssets().push_back(body_9_80_shape) 
body_9.GetAssets().push_back(body_9_80_level) 

# Visualization shape 
body_9_81_shape = chrono.ChObjShapeFile() 
body_9_81_shape.SetFilename(shapes_dir +'body_9_81.obj') 
body_9_81_level = chrono.ChAssetLevel() 
body_9_81_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_81_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_81_level.GetAssets().push_back(body_9_81_shape) 
body_9.GetAssets().push_back(body_9_81_level) 

# Visualization shape 
body_9_82_shape = chrono.ChObjShapeFile() 
body_9_82_shape.SetFilename(shapes_dir +'body_9_82.obj') 
body_9_82_level = chrono.ChAssetLevel() 
body_9_82_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_82_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_82_level.GetAssets().push_back(body_9_82_shape) 
body_9.GetAssets().push_back(body_9_82_level) 

# Visualization shape 
body_9_83_shape = chrono.ChObjShapeFile() 
body_9_83_shape.SetFilename(shapes_dir +'body_9_83.obj') 
body_9_83_level = chrono.ChAssetLevel() 
body_9_83_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_83_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_83_level.GetAssets().push_back(body_9_83_shape) 
body_9.GetAssets().push_back(body_9_83_level) 

# Visualization shape 
body_9_84_shape = chrono.ChObjShapeFile() 
body_9_84_shape.SetFilename(shapes_dir +'body_9_84.obj') 
body_9_84_level = chrono.ChAssetLevel() 
body_9_84_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_84_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_84_level.GetAssets().push_back(body_9_84_shape) 
body_9.GetAssets().push_back(body_9_84_level) 

# Visualization shape 
body_9_85_shape = chrono.ChObjShapeFile() 
body_9_85_shape.SetFilename(shapes_dir +'body_9_85.obj') 
body_9_85_level = chrono.ChAssetLevel() 
body_9_85_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_85_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_85_level.GetAssets().push_back(body_9_85_shape) 
body_9.GetAssets().push_back(body_9_85_level) 

# Visualization shape 
body_9_86_shape = chrono.ChObjShapeFile() 
body_9_86_shape.SetFilename(shapes_dir +'body_9_86.obj') 
body_9_86_level = chrono.ChAssetLevel() 
body_9_86_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_86_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_86_level.GetAssets().push_back(body_9_86_shape) 
body_9.GetAssets().push_back(body_9_86_level) 

# Visualization shape 
body_9_87_shape = chrono.ChObjShapeFile() 
body_9_87_shape.SetFilename(shapes_dir +'body_9_87.obj') 
body_9_87_level = chrono.ChAssetLevel() 
body_9_87_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_87_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_87_level.GetAssets().push_back(body_9_87_shape) 
body_9.GetAssets().push_back(body_9_87_level) 

# Visualization shape 
body_9_88_shape = chrono.ChObjShapeFile() 
body_9_88_shape.SetFilename(shapes_dir +'body_9_88.obj') 
body_9_88_level = chrono.ChAssetLevel() 
body_9_88_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_88_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_88_level.GetAssets().push_back(body_9_88_shape) 
body_9.GetAssets().push_back(body_9_88_level) 

# Visualization shape 
body_9_89_shape = chrono.ChObjShapeFile() 
body_9_89_shape.SetFilename(shapes_dir +'body_9_89.obj') 
body_9_89_level = chrono.ChAssetLevel() 
body_9_89_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_89_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_89_level.GetAssets().push_back(body_9_89_shape) 
body_9.GetAssets().push_back(body_9_89_level) 

# Visualization shape 
body_9_90_shape = chrono.ChObjShapeFile() 
body_9_90_shape.SetFilename(shapes_dir +'body_9_90.obj') 
body_9_90_level = chrono.ChAssetLevel() 
body_9_90_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_90_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_90_level.GetAssets().push_back(body_9_90_shape) 
body_9.GetAssets().push_back(body_9_90_level) 

# Visualization shape 
body_9_91_shape = chrono.ChObjShapeFile() 
body_9_91_shape.SetFilename(shapes_dir +'body_9_91.obj') 
body_9_91_level = chrono.ChAssetLevel() 
body_9_91_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_91_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_91_level.GetAssets().push_back(body_9_91_shape) 
body_9.GetAssets().push_back(body_9_91_level) 

# Visualization shape 
body_9_92_shape = chrono.ChObjShapeFile() 
body_9_92_shape.SetFilename(shapes_dir +'body_9_92.obj') 
body_9_92_level = chrono.ChAssetLevel() 
body_9_92_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_92_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_92_level.GetAssets().push_back(body_9_92_shape) 
body_9.GetAssets().push_back(body_9_92_level) 

# Visualization shape 
body_9_93_shape = chrono.ChObjShapeFile() 
body_9_93_shape.SetFilename(shapes_dir +'body_9_93.obj') 
body_9_93_level = chrono.ChAssetLevel() 
body_9_93_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_93_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_93_level.GetAssets().push_back(body_9_93_shape) 
body_9.GetAssets().push_back(body_9_93_level) 

# Visualization shape 
body_9_94_shape = chrono.ChObjShapeFile() 
body_9_94_shape.SetFilename(shapes_dir +'body_9_94.obj') 
body_9_94_level = chrono.ChAssetLevel() 
body_9_94_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_94_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_94_level.GetAssets().push_back(body_9_94_shape) 
body_9.GetAssets().push_back(body_9_94_level) 

# Visualization shape 
body_9_95_shape = chrono.ChObjShapeFile() 
body_9_95_shape.SetFilename(shapes_dir +'body_9_95.obj') 
body_9_95_level = chrono.ChAssetLevel() 
body_9_95_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_95_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_95_level.GetAssets().push_back(body_9_95_shape) 
body_9.GetAssets().push_back(body_9_95_level) 

# Visualization shape 
body_9_96_shape = chrono.ChObjShapeFile() 
body_9_96_shape.SetFilename(shapes_dir +'body_9_96.obj') 
body_9_96_level = chrono.ChAssetLevel() 
body_9_96_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_96_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_96_level.GetAssets().push_back(body_9_96_shape) 
body_9.GetAssets().push_back(body_9_96_level) 

# Visualization shape 
body_9_97_shape = chrono.ChObjShapeFile() 
body_9_97_shape.SetFilename(shapes_dir +'body_9_97.obj') 
body_9_97_level = chrono.ChAssetLevel() 
body_9_97_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_97_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_97_level.GetAssets().push_back(body_9_97_shape) 
body_9.GetAssets().push_back(body_9_97_level) 

# Visualization shape 
body_9_98_shape = chrono.ChObjShapeFile() 
body_9_98_shape.SetFilename(shapes_dir +'body_9_98.obj') 
body_9_98_level = chrono.ChAssetLevel() 
body_9_98_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_98_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_98_level.GetAssets().push_back(body_9_98_shape) 
body_9.GetAssets().push_back(body_9_98_level) 

# Visualization shape 
body_9_99_shape = chrono.ChObjShapeFile() 
body_9_99_shape.SetFilename(shapes_dir +'body_9_99.obj') 
body_9_99_level = chrono.ChAssetLevel() 
body_9_99_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_99_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_99_level.GetAssets().push_back(body_9_99_shape) 
body_9.GetAssets().push_back(body_9_99_level) 

# Visualization shape 
body_9_100_shape = chrono.ChObjShapeFile() 
body_9_100_shape.SetFilename(shapes_dir +'body_9_100.obj') 
body_9_100_level = chrono.ChAssetLevel() 
body_9_100_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_100_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_100_level.GetAssets().push_back(body_9_100_shape) 
body_9.GetAssets().push_back(body_9_100_level) 

# Visualization shape 
body_9_101_shape = chrono.ChObjShapeFile() 
body_9_101_shape.SetFilename(shapes_dir +'body_9_101.obj') 
body_9_101_level = chrono.ChAssetLevel() 
body_9_101_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_101_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_101_level.GetAssets().push_back(body_9_101_shape) 
body_9.GetAssets().push_back(body_9_101_level) 

# Visualization shape 
body_9_102_shape = chrono.ChObjShapeFile() 
body_9_102_shape.SetFilename(shapes_dir +'body_9_102.obj') 
body_9_102_level = chrono.ChAssetLevel() 
body_9_102_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_102_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_102_level.GetAssets().push_back(body_9_102_shape) 
body_9.GetAssets().push_back(body_9_102_level) 

# Visualization shape 
body_9_103_shape = chrono.ChObjShapeFile() 
body_9_103_shape.SetFilename(shapes_dir +'body_9_103.obj') 
body_9_103_level = chrono.ChAssetLevel() 
body_9_103_level.GetFrame().SetPos(chrono.ChVectorD(-0.059368852360613,0.0440140219884158,0.042000000050556)) 
body_9_103_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_103_level.GetAssets().push_back(body_9_103_shape) 
body_9.GetAssets().push_back(body_9_103_level) 

# Visualization shape 
body_9_67_shape = chrono.ChObjShapeFile() 
body_9_67_shape.SetFilename(shapes_dir +'body_9_67.obj') 
body_9_67_level = chrono.ChAssetLevel() 
body_9_67_level.GetFrame().SetPos(chrono.ChVectorD(-0.0406742354800063,0.0605090424396713,0.039235000050556)) 
body_9_67_level.GetFrame().SetRot(chrono.ChQuaternionD(0.009255741791487,0.707046201633167,0.009255741791487,-0.707046201633167)) 
body_9_67_level.GetAssets().push_back(body_9_67_shape) 
body_9.GetAssets().push_back(body_9_67_level) 

# Visualization shape 
body_9_77_shape = chrono.ChObjShapeFile() 
body_9_77_shape.SetFilename(shapes_dir +'body_9_77.obj') 
body_9_77_level = chrono.ChAssetLevel() 
body_9_77_level.GetFrame().SetPos(chrono.ChVectorD(-0.040228923325746,0.0580198463675893,0.013000000050556)) 
body_9_77_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_77_level.GetAssets().push_back(body_9_77_shape) 
body_9.GetAssets().push_back(body_9_77_level) 

# Visualization shape 
body_9_68_shape = chrono.ChObjShapeFile() 
body_9_68_shape.SetFilename(shapes_dir +'body_9_68.obj') 
body_9_68_level = chrono.ChAssetLevel() 
body_9_68_level.GetFrame().SetPos(chrono.ChVectorD(-0.0412890897614698,0.0985059691463034,0.030500000139963)) 
body_9_68_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_68_level.GetAssets().push_back(body_9_68_shape) 
body_9.GetAssets().push_back(body_9_68_level) 

# Visualization shape 
body_9_66_shape = chrono.ChObjShapeFile() 
body_9_66_shape.SetFilename(shapes_dir +'body_9_66.obj') 
body_9_66_level = chrono.ChAssetLevel() 
body_9_66_level.GetFrame().SetPos(chrono.ChVectorD(-0.041864982624243,0.120498430295766,0.046500000139963)) 
body_9_66_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_66_level.GetAssets().push_back(body_9_66_shape) 
body_9.GetAssets().push_back(body_9_66_level) 

# Visualization shape 
body_9_66_shape = chrono.ChObjShapeFile() 
body_9_66_shape.SetFilename(shapes_dir +'body_9_66.obj') 
body_9_66_level = chrono.ChAssetLevel() 
body_9_66_level.GetFrame().SetPos(chrono.ChVectorD(-0.041864982624243,0.120498430295766,0.036500000139963)) 
body_9_66_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_66_level.GetAssets().push_back(body_9_66_shape) 
body_9.GetAssets().push_back(body_9_66_level) 

# Visualization shape 
body_9_109_shape = chrono.ChObjShapeFile() 
body_9_109_shape.SetFilename(shapes_dir +'body_9_109.obj') 
body_9_109_level = chrono.ChAssetLevel() 
body_9_109_level.GetFrame().SetPos(chrono.ChVectorD(-0.0363268466341977,0.0236101995008563,0.018850000050556)) 
body_9_109_level.GetFrame().SetRot(chrono.ChQuaternionD(1.37662076806858E-31,0.69779045984168,0.716301943424654,3.01135793015002E-32)) 
body_9_109_level.GetAssets().push_back(body_9_109_shape) 
body_9.GetAssets().push_back(body_9_109_level) 

# Visualization shape 
body_9_109_shape = chrono.ChObjShapeFile() 
body_9_109_shape.SetFilename(shapes_dir +'body_9_109.obj') 
body_9_109_level = chrono.ChAssetLevel() 
body_9_109_level.GetFrame().SetPos(chrono.ChVectorD(-0.0363268466341977,0.0236101995008562,0.040150000050556)) 
body_9_109_level.GetFrame().SetRot(chrono.ChQuaternionD(0.716301943424654,1.04668568976252E-15,1.07445291513698E-15,-0.69779045984168)) 
body_9_109_level.GetAssets().push_back(body_9_109_shape) 
body_9.GetAssets().push_back(body_9_109_level) 

# Visualization shape 
body_9_111_shape = chrono.ChObjShapeFile() 
body_9_111_shape.SetFilename(shapes_dir +'body_9_111.obj') 
body_9_111_level = chrono.ChAssetLevel() 
body_9_111_level.GetFrame().SetPos(chrono.ChVectorD(-0.0407262853435955,0.0770133355421249,-0.001499999949444)) 
body_9_111_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.01135793015002E-32,0.716301943424654,-0.69779045984168,1.37662076806858E-31)) 
body_9_111_level.GetAssets().push_back(body_9_111_shape) 
body_9.GetAssets().push_back(body_9_111_level) 

# Visualization shape 
body_9_112_shape = chrono.ChObjShapeFile() 
body_9_112_shape.SetFilename(shapes_dir +'body_9_112.obj') 
body_9_112_level = chrono.ChAssetLevel() 
body_9_112_level.GetFrame().SetPos(chrono.ChVectorD(0.0909047274640663,-0.012330645692924,0.0395)) 
body_9_112_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.493412366001331,-0.493412366001331,0.506501961572676,0.506501961572676)) 
body_9_112_level.GetAssets().push_back(body_9_112_shape) 
body_9.GetAssets().push_back(body_9_112_level) 

# Visualization shape 
body_9_113_shape = chrono.ChObjShapeFile() 
body_9_113_shape.SetFilename(shapes_dir +'body_9_113.obj') 
body_9_113_level = chrono.ChAssetLevel() 
body_9_113_level.GetFrame().SetPos(chrono.ChVectorD(0.109782684588705,-0.0129025099651384,0.121496520696944)) 
body_9_113_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.493070629011337,-0.493753866468332,0.506852521607917,0.50615115873979)) 
body_9_113_level.GetAssets().push_back(body_9_113_shape) 
body_9.GetAssets().push_back(body_9_113_level) 

# Visualization shape 
body_9_114_shape = chrono.ChObjShapeFile() 
body_9_114_shape.SetFilename(shapes_dir +'body_9_114.obj') 
body_9_114_level = chrono.ChAssetLevel() 
body_9_114_level.GetFrame().SetPos(chrono.ChVectorD(0.056587794727428,-0.01138222272039,0.05103)) 
body_9_114_level.GetFrame().SetRot(chrono.ChQuaternionD(0,-0.69779045984168,0.716301943424654,3.01135793015002E-32)) 
body_9_114_level.GetAssets().push_back(body_9_114_shape) 
body_9.GetAssets().push_back(body_9_114_level) 

# Visualization shape 
body_9_115_shape = chrono.ChObjShapeFile() 
body_9_115_shape.SetFilename(shapes_dir +'body_9_115.obj') 
body_9_115_level = chrono.ChAssetLevel() 
body_9_115_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_115_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_115_level.GetAssets().push_back(body_9_115_shape) 
body_9.GetAssets().push_back(body_9_115_level) 

# Visualization shape 
body_9_116_shape = chrono.ChObjShapeFile() 
body_9_116_shape.SetFilename(shapes_dir +'body_9_116.obj') 
body_9_116_level = chrono.ChAssetLevel() 
body_9_116_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,-0.127500000000001,0.05)) 
body_9_116_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_116_level.GetAssets().push_back(body_9_116_shape) 
body_9.GetAssets().push_back(body_9_116_level) 

# Visualization shape 
body_9_117_shape = chrono.ChObjShapeFile() 
body_9_117_shape.SetFilename(shapes_dir +'body_9_117.obj') 
body_9_117_level = chrono.ChAssetLevel() 
body_9_117_level.GetFrame().SetPos(chrono.ChVectorD(-0.0495,-0.121400000000001,0.022)) 
body_9_117_level.GetFrame().SetRot(chrono.ChQuaternionD(-3.88908729652601E-15,0.707106781186547,3.88908729652601E-15,0.707106781186548)) 
body_9_117_level.GetAssets().push_back(body_9_117_shape) 
body_9.GetAssets().push_back(body_9_117_level) 

# Visualization shape 
body_9_118_shape = chrono.ChObjShapeFile() 
body_9_118_shape.SetFilename(shapes_dir +'body_9_118.obj') 
body_9_118_level = chrono.ChAssetLevel() 
body_9_118_level.GetFrame().SetPos(chrono.ChVectorD(0.02529,0.0564000000000001,0.017450002515675)) 
body_9_118_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-7.07106781186548E-16,-7.07106781186548E-16)) 
body_9_118_level.GetAssets().push_back(body_9_118_shape) 
body_9.GetAssets().push_back(body_9_118_level) 

# Visualization shape 
body_9_119_shape = chrono.ChObjShapeFile() 
body_9_119_shape.SetFilename(shapes_dir +'body_9_119.obj') 
body_9_119_level = chrono.ChAssetLevel() 
body_9_119_level.GetFrame().SetPos(chrono.ChVectorD(0.04029,0.022,0.017450002515675)) 
body_9_119_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_119_level.GetAssets().push_back(body_9_119_shape) 
body_9.GetAssets().push_back(body_9_119_level) 

# Visualization shape 
body_9_120_shape = chrono.ChObjShapeFile() 
body_9_120_shape.SetFilename(shapes_dir +'body_9_120.obj') 
body_9_120_level = chrono.ChAssetLevel() 
body_9_120_level.GetFrame().SetPos(chrono.ChVectorD(0.02729,0.0309,0.018250002515675)) 
body_9_120_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_120_level.GetAssets().push_back(body_9_120_shape) 
body_9.GetAssets().push_back(body_9_120_level) 

# Visualization shape 
body_9_121_shape = chrono.ChObjShapeFile() 
body_9_121_shape.SetFilename(shapes_dir +'body_9_121.obj') 
body_9_121_level = chrono.ChAssetLevel() 
body_9_121_level.GetFrame().SetPos(chrono.ChVectorD(0.02829,0.0364,0.017450002515675)) 
body_9_121_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_121_level.GetAssets().push_back(body_9_121_shape) 
body_9.GetAssets().push_back(body_9_121_level) 

# Visualization shape 
body_9_122_shape = chrono.ChObjShapeFile() 
body_9_122_shape.SetFilename(shapes_dir +'body_9_122.obj') 
body_9_122_level = chrono.ChAssetLevel() 
body_9_122_level.GetFrame().SetPos(chrono.ChVectorD(0.02879,0.0199,0.017450002515675)) 
body_9_122_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_122_level.GetAssets().push_back(body_9_122_shape) 
body_9.GetAssets().push_back(body_9_122_level) 

# Visualization shape 
body_9_123_shape = chrono.ChObjShapeFile() 
body_9_123_shape.SetFilename(shapes_dir +'body_9_123.obj') 
body_9_123_level = chrono.ChAssetLevel() 
body_9_123_level.GetFrame().SetPos(chrono.ChVectorD(0.02579,0.0484000000000001,0.017450002515675)) 
body_9_123_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_123_level.GetAssets().push_back(body_9_123_shape) 
body_9.GetAssets().push_back(body_9_123_level) 

# Visualization shape 
body_9_124_shape = chrono.ChObjShapeFile() 
body_9_124_shape.SetFilename(shapes_dir +'body_9_124.obj') 
body_9_124_level = chrono.ChAssetLevel() 
body_9_124_level.GetFrame().SetPos(chrono.ChVectorD(0.04229,0.051,0.015600002515675)) 
body_9_124_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_124_level.GetAssets().push_back(body_9_124_shape) 
body_9.GetAssets().push_back(body_9_124_level) 

# Visualization shape 
body_9_125_shape = chrono.ChObjShapeFile() 
body_9_125_shape.SetFilename(shapes_dir +'body_9_125.obj') 
body_9_125_level = chrono.ChAssetLevel() 
body_9_125_level.GetFrame().SetPos(chrono.ChVectorD(0.03499,0.00600000000000006,0.017450002515675)) 
body_9_125_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_125_level.GetAssets().push_back(body_9_125_shape) 
body_9.GetAssets().push_back(body_9_125_level) 

# Visualization shape 
body_9_126_shape = chrono.ChObjShapeFile() 
body_9_126_shape.SetFilename(shapes_dir +'body_9_126.obj') 
body_9_126_level = chrono.ChAssetLevel() 
body_9_126_level.GetFrame().SetPos(chrono.ChVectorD(0.02829,0.00790000000000002,0.017450002515675)) 
body_9_126_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-7.07106781186548E-16,-7.07106781186548E-16)) 
body_9_126_level.GetAssets().push_back(body_9_126_shape) 
body_9.GetAssets().push_back(body_9_126_level) 

# Visualization shape 
body_9_127_shape = chrono.ChObjShapeFile() 
body_9_127_shape.SetFilename(shapes_dir +'body_9_127.obj') 
body_9_127_level = chrono.ChAssetLevel() 
body_9_127_level.GetFrame().SetPos(chrono.ChVectorD(0.03479,0.0104,0.017450002515675)) 
body_9_127_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_127_level.GetAssets().push_back(body_9_127_shape) 
body_9.GetAssets().push_back(body_9_127_level) 

# Visualization shape 
body_9_128_shape = chrono.ChObjShapeFile() 
body_9_128_shape.SetFilename(shapes_dir +'body_9_128.obj') 
body_9_128_level = chrono.ChAssetLevel() 
body_9_128_level.GetFrame().SetPos(chrono.ChVectorD(0.03929,0.0419,0.017450002515675)) 
body_9_128_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_128_level.GetAssets().push_back(body_9_128_shape) 
body_9.GetAssets().push_back(body_9_128_level) 

# Visualization shape 
body_9_119_shape = chrono.ChObjShapeFile() 
body_9_119_shape.SetFilename(shapes_dir +'body_9_119.obj') 
body_9_119_level = chrono.ChAssetLevel() 
body_9_119_level.GetFrame().SetPos(chrono.ChVectorD(0.04029,0.00940000000000002,0.017450002515675)) 
body_9_119_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_119_level.GetAssets().push_back(body_9_119_shape) 
body_9.GetAssets().push_back(body_9_119_level) 

# Visualization shape 
body_9_130_shape = chrono.ChObjShapeFile() 
body_9_130_shape.SetFilename(shapes_dir +'body_9_130.obj') 
body_9_130_level = chrono.ChAssetLevel() 
body_9_130_level.GetFrame().SetPos(chrono.ChVectorD(0.03509,0.00340000000000007,0.017450002515675)) 
body_9_130_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_130_level.GetAssets().push_back(body_9_130_shape) 
body_9.GetAssets().push_back(body_9_130_level) 

# Visualization shape 
body_9_131_shape = chrono.ChObjShapeFile() 
body_9_131_shape.SetFilename(shapes_dir +'body_9_131.obj') 
body_9_131_level = chrono.ChAssetLevel() 
body_9_131_level.GetFrame().SetPos(chrono.ChVectorD(0.02729,0.00215000000000004,0.017430002515675)) 
body_9_131_level.GetFrame().SetRot(chrono.ChQuaternionD(7.07106781186548E-16,7.07106781186548E-16,0.707106781186548,-0.707106781186547)) 
body_9_131_level.GetAssets().push_back(body_9_131_shape) 
body_9.GetAssets().push_back(body_9_131_level) 

# Visualization shape 
body_9_132_shape = chrono.ChObjShapeFile() 
body_9_132_shape.SetFilename(shapes_dir +'body_9_132.obj') 
body_9_132_level = chrono.ChAssetLevel() 
body_9_132_level.GetFrame().SetPos(chrono.ChVectorD(0.031089999967217,0.0439,0.026750002512695)) 
body_9_132_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,7.07106781186548E-16,-7.07106781186548E-16,-0.707106781186547)) 
body_9_132_level.GetAssets().push_back(body_9_132_shape) 
body_9.GetAssets().push_back(body_9_132_level) 

# Visualization shape 
body_9_133_shape = chrono.ChObjShapeFile() 
body_9_133_shape.SetFilename(shapes_dir +'body_9_133.obj') 
body_9_133_level = chrono.ChAssetLevel() 
body_9_133_level.GetFrame().SetPos(chrono.ChVectorD(0.02369,0.0109,0.017450002515675)) 
body_9_133_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_133_level.GetAssets().push_back(body_9_133_shape) 
body_9.GetAssets().push_back(body_9_133_level) 

# Visualization shape 
body_9_134_shape = chrono.ChObjShapeFile() 
body_9_134_shape.SetFilename(shapes_dir +'body_9_134.obj') 
body_9_134_level = chrono.ChAssetLevel() 
body_9_134_level.GetFrame().SetPos(chrono.ChVectorD(0.02009,0.0161000000000001,0.017450002515675)) 
body_9_134_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_134_level.GetAssets().push_back(body_9_134_shape) 
body_9.GetAssets().push_back(body_9_134_level) 

# Visualization shape 
body_9_135_shape = chrono.ChObjShapeFile() 
body_9_135_shape.SetFilename(shapes_dir +'body_9_135.obj') 
body_9_135_level = chrono.ChAssetLevel() 
body_9_135_level.GetFrame().SetPos(chrono.ChVectorD(0.02529,0.00640000000000002,0.017450002515675)) 
body_9_135_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.500000000000001)) 
body_9_135_level.GetAssets().push_back(body_9_135_shape) 
body_9.GetAssets().push_back(body_9_135_level) 

# Visualization shape 
body_9_57_shape = chrono.ChObjShapeFile() 
body_9_57_shape.SetFilename(shapes_dir +'body_9_57.obj') 
body_9_57_level = chrono.ChAssetLevel() 
body_9_57_level.GetFrame().SetPos(chrono.ChVectorD(-0.084624521612719,0.034349593881785,0.0285)) 
body_9_57_level.GetFrame().SetRot(chrono.ChQuaternionD(0.506501961572676,0.506501961572676,-0.493412366001331,-0.493412366001331)) 
body_9_57_level.GetAssets().push_back(body_9_57_shape) 
body_9.GetAssets().push_back(body_9_57_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.040347940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.052641897313779,-0.126293067475934,0.029780768066139)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.034891897313778,-0.126293067475934,0.026580768066139)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.033747940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.044747940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.050447940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.035947940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.042547940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.052647940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_146_shape = chrono.ChObjShapeFile() 
body_9_146_shape.SetFilename(shapes_dir +'body_9_146.obj') 
body_9_146_level = chrono.ChAssetLevel() 
body_9_146_level.GetFrame().SetPos(chrono.ChVectorD(0.04055,-0.126306051264622,0.035078643996917)) 
body_9_146_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0)) 
body_9_146_level.GetAssets().push_back(body_9_146_shape) 
body_9.GetAssets().push_back(body_9_146_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.054847940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.038147940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.046947940300436,-0.126293067475934,0.022526838604685)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.052641897313779,-0.126293067475934,0.027580768066139)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_151_shape = chrono.ChObjShapeFile() 
body_9_151_shape.SetFilename(shapes_dir +'body_9_151.obj') 
body_9_151_level = chrono.ChAssetLevel() 
body_9_151_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_151_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_151_level.GetAssets().push_back(body_9_151_shape) 
body_9.GetAssets().push_back(body_9_151_level) 

# Visualization shape 
body_9_152_shape = chrono.ChObjShapeFile() 
body_9_152_shape.SetFilename(shapes_dir +'body_9_152.obj') 
body_9_152_level = chrono.ChAssetLevel() 
body_9_152_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_152_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_152_level.GetAssets().push_back(body_9_152_shape) 
body_9.GetAssets().push_back(body_9_152_level) 

# Visualization shape 
body_9_153_shape = chrono.ChObjShapeFile() 
body_9_153_shape.SetFilename(shapes_dir +'body_9_153.obj') 
body_9_153_level = chrono.ChAssetLevel() 
body_9_153_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_153_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_153_level.GetAssets().push_back(body_9_153_shape) 
body_9.GetAssets().push_back(body_9_153_level) 

# Visualization shape 
body_9_154_shape = chrono.ChObjShapeFile() 
body_9_154_shape.SetFilename(shapes_dir +'body_9_154.obj') 
body_9_154_level = chrono.ChAssetLevel() 
body_9_154_level.GetFrame().SetPos(chrono.ChVectorD(0.043394164236971,-0.126300000000001,0.026629822914549)) 
body_9_154_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_9_154_level.GetAssets().push_back(body_9_154_shape) 
body_9.GetAssets().push_back(body_9_154_level) 

# Visualization shape 
body_9_155_shape = chrono.ChObjShapeFile() 
body_9_155_shape.SetFilename(shapes_dir +'body_9_155.obj') 
body_9_155_level = chrono.ChAssetLevel() 
body_9_155_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_155_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_155_level.GetAssets().push_back(body_9_155_shape) 
body_9.GetAssets().push_back(body_9_155_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.034891897313778,-0.126293067475934,0.028780768066139)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_157_shape = chrono.ChObjShapeFile() 
body_9_157_shape.SetFilename(shapes_dir +'body_9_157.obj') 
body_9_157_level = chrono.ChAssetLevel() 
body_9_157_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_157_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_157_level.GetAssets().push_back(body_9_157_shape) 
body_9.GetAssets().push_back(body_9_157_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.044350878876574,-0.126293067475934,0.031780973671959)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_137_shape = chrono.ChObjShapeFile() 
body_9_137_shape.SetFilename(shapes_dir +'body_9_137.obj') 
body_9_137_level = chrono.ChAssetLevel() 
body_9_137_level.GetFrame().SetPos(chrono.ChVectorD(0.042350741806027,-0.126293067475934,0.029822506123715)) 
body_9_137_level.GetFrame().SetRot(chrono.ChQuaternionD(2.46885013108226E-15,-2.46885013108227E-15,0.707106781186549,0.707106781186546)) 
body_9_137_level.GetAssets().push_back(body_9_137_shape) 
body_9.GetAssets().push_back(body_9_137_level) 

# Visualization shape 
body_9_160_shape = chrono.ChObjShapeFile() 
body_9_160_shape.SetFilename(shapes_dir +'body_9_160.obj') 
body_9_160_level = chrono.ChAssetLevel() 
body_9_160_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_160_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_160_level.GetAssets().push_back(body_9_160_shape) 
body_9.GetAssets().push_back(body_9_160_level) 

# Visualization shape 
body_9_161_shape = chrono.ChObjShapeFile() 
body_9_161_shape.SetFilename(shapes_dir +'body_9_161.obj') 
body_9_161_level = chrono.ChAssetLevel() 
body_9_161_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_161_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_161_level.GetAssets().push_back(body_9_161_shape) 
body_9.GetAssets().push_back(body_9_161_level) 

# Visualization shape 
body_9_162_shape = chrono.ChObjShapeFile() 
body_9_162_shape.SetFilename(shapes_dir +'body_9_162.obj') 
body_9_162_level = chrono.ChAssetLevel() 
body_9_162_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_162_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_162_level.GetAssets().push_back(body_9_162_shape) 
body_9.GetAssets().push_back(body_9_162_level) 

# Visualization shape 
body_9_163_shape = chrono.ChObjShapeFile() 
body_9_163_shape.SetFilename(shapes_dir +'body_9_163.obj') 
body_9_163_level = chrono.ChAssetLevel() 
body_9_163_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_163_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_163_level.GetAssets().push_back(body_9_163_shape) 
body_9.GetAssets().push_back(body_9_163_level) 

# Visualization shape 
body_9_164_shape = chrono.ChObjShapeFile() 
body_9_164_shape.SetFilename(shapes_dir +'body_9_164.obj') 
body_9_164_level = chrono.ChAssetLevel() 
body_9_164_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_164_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_164_level.GetAssets().push_back(body_9_164_shape) 
body_9.GetAssets().push_back(body_9_164_level) 

# Visualization shape 
body_9_165_shape = chrono.ChObjShapeFile() 
body_9_165_shape.SetFilename(shapes_dir +'body_9_165.obj') 
body_9_165_level = chrono.ChAssetLevel() 
body_9_165_level.GetFrame().SetPos(chrono.ChVectorD(0.0443,-0.126300000000001,0.023)) 
body_9_165_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0)) 
body_9_165_level.GetAssets().push_back(body_9_165_shape) 
body_9.GetAssets().push_back(body_9_165_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.07605298109793,0.050829617947409,0.04475)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148594,0.707046201633167,-0.00925574179148524,0.707046201633167)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.034848604305766,0.0626622775456731,0.049000000050555)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.076052981097942,0.050829617947409,0.01225)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.033435049097141,0.00868078199699307,0.049000000050555)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,-0.07033,0.035)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.075202230277936,0.018340754885703,0.01225)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.075202230277924,0.018340754885703,0.04475)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148594,0.707046201633167,-0.00925574179148524,0.707046201633167)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.075202230277924,0.018340754885703,0.01225)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148594,0.707046201633167,-0.00925574179148524,0.707046201633167)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.07953,0.04225)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.040582598970716,0.00849361681659105,0.049000000050556)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.00460000000000005,0.035)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.076052981097942,0.050829617947409,0.04475)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_7_shape = chrono.ChObjShapeFile() 
body_9_7_shape.SetFilename(shapes_dir +'body_9_7.obj') 
body_9_7_level = chrono.ChAssetLevel() 
body_9_7_level.GetFrame().SetPos(chrono.ChVectorD(0.0485,-0.131199999698941,0.0539999999999999)) 
body_9_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186549,0.707106781186546,-4.95433823295186E-46,0)) 
body_9_7_level.GetAssets().push_back(body_9_7_shape) 
body_9.GetAssets().push_back(body_9_7_level) 

# Visualization shape 
body_9_8_shape = chrono.ChObjShapeFile() 
body_9_8_shape.SetFilename(shapes_dir +'body_9_8.obj') 
body_9_8_level = chrono.ChAssetLevel() 
body_9_8_level.GetFrame().SetPos(chrono.ChVectorD(0.05002,-0.131000000000001,0.0537499999999999)) 
body_9_8_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_8_level.GetAssets().push_back(body_9_8_shape) 
body_9.GetAssets().push_back(body_9_8_level) 

# Visualization shape 
body_9_5_shape = chrono.ChObjShapeFile() 
body_9_5_shape.SetFilename(shapes_dir +'body_9_5.obj') 
body_9_5_level = chrono.ChAssetLevel() 
body_9_5_level.GetFrame().SetPos(chrono.ChVectorD(0.04698,-0.119000000000001,0.0537499999999999)) 
body_9_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_5_level.GetAssets().push_back(body_9_5_shape) 
body_9.GetAssets().push_back(body_9_5_level) 

# Visualization shape 
body_9_9_shape = chrono.ChObjShapeFile() 
body_9_9_shape.SetFilename(shapes_dir +'body_9_9.obj') 
body_9_9_level = chrono.ChAssetLevel() 
body_9_9_level.GetFrame().SetPos(chrono.ChVectorD(0.04952,-0.131050000000001,0.0540499999999999)) 
body_9_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-1.06066017177982E-15,-3.53553390593272E-16,0.707106781186548,-0.707106781186547)) 
body_9_9_level.GetAssets().push_back(body_9_9_shape) 
body_9.GetAssets().push_back(body_9_9_level) 

# Visualization shape 
body_9_6_shape = chrono.ChObjShapeFile() 
body_9_6_shape.SetFilename(shapes_dir +'body_9_6.obj') 
body_9_6_level = chrono.ChAssetLevel() 
body_9_6_level.GetFrame().SetPos(chrono.ChVectorD(0.048,-0.131050000000001,0.0539999999999999)) 
body_9_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.25280609221184,4.29650775268414E-16,0.967516966125441,-5.91271212405635E-16)) 
body_9_6_level.GetAssets().push_back(body_9_6_shape) 
body_9.GetAssets().push_back(body_9_6_level) 

# Visualization shape 
body_9_7_shape = chrono.ChObjShapeFile() 
body_9_7_shape.SetFilename(shapes_dir +'body_9_7.obj') 
body_9_7_level = chrono.ChAssetLevel() 
body_9_7_level.GetFrame().SetPos(chrono.ChVectorD(0.0405,-0.131199999698941,0.0539999999999999)) 
body_9_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186549,0.707106781186546,-4.95433823295186E-46,0)) 
body_9_7_level.GetAssets().push_back(body_9_7_shape) 
body_9.GetAssets().push_back(body_9_7_level) 

# Visualization shape 
body_9_5_shape = chrono.ChObjShapeFile() 
body_9_5_shape.SetFilename(shapes_dir +'body_9_5.obj') 
body_9_5_level = chrono.ChAssetLevel() 
body_9_5_level.GetFrame().SetPos(chrono.ChVectorD(0.03898,-0.119000000000001,0.0537499999999999)) 
body_9_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_5_level.GetAssets().push_back(body_9_5_shape) 
body_9.GetAssets().push_back(body_9_5_level) 

# Visualization shape 
body_9_6_shape = chrono.ChObjShapeFile() 
body_9_6_shape.SetFilename(shapes_dir +'body_9_6.obj') 
body_9_6_level = chrono.ChAssetLevel() 
body_9_6_level.GetFrame().SetPos(chrono.ChVectorD(0.04,-0.131050000000001,0.0539999999999999)) 
body_9_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.25280609221184,4.29650775268414E-16,0.967516966125441,-5.91271212405635E-16)) 
body_9_6_level.GetAssets().push_back(body_9_6_shape) 
body_9.GetAssets().push_back(body_9_6_level) 

# Visualization shape 
body_9_9_shape = chrono.ChObjShapeFile() 
body_9_9_shape.SetFilename(shapes_dir +'body_9_9.obj') 
body_9_9_level = chrono.ChAssetLevel() 
body_9_9_level.GetFrame().SetPos(chrono.ChVectorD(0.04152,-0.131050000000001,0.0540499999999999)) 
body_9_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-1.06066017177982E-15,-3.53553390593272E-16,0.707106781186548,-0.707106781186547)) 
body_9_9_level.GetAssets().push_back(body_9_9_shape) 
body_9.GetAssets().push_back(body_9_9_level) 

# Visualization shape 
body_9_8_shape = chrono.ChObjShapeFile() 
body_9_8_shape.SetFilename(shapes_dir +'body_9_8.obj') 
body_9_8_level = chrono.ChAssetLevel() 
body_9_8_level.GetFrame().SetPos(chrono.ChVectorD(0.04202,-0.131000000000001,0.0537499999999999)) 
body_9_8_level.GetFrame().SetRot(chrono.ChQuaternionD(-7.07106781186546E-16,9.76165567115787E-31,0.707106781186548,-0.707106781186547)) 
body_9_8_level.GetAssets().push_back(body_9_8_shape) 
body_9.GetAssets().push_back(body_9_8_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.07953,0.035)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_9.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.041996154179341,0.062475112365271,0.049000000050556)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_9_190_shape = chrono.ChObjShapeFile() 
body_9_190_shape.SetFilename(shapes_dir +'body_9_190.obj') 
body_9_190_level = chrono.ChAssetLevel() 
body_9_190_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_190_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_190_level.GetAssets().push_back(body_9_190_shape) 
body_9.GetAssets().push_back(body_9_190_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(-0.082550753710283,0.050659467783408,0.01225)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.00925574179148701)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(0.082550753710271,0.050659467783408,0.04475)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148559,0.707046201633167,-0.00925574179148559,0.707046201633167)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.00459999999999999,0.04225)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(0.081700002890265,0.018170604721702,0.01225)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148524,0.707046201633168,-0.00925574179148594,0.707046201633167)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(-0.082550753710283,0.050659467783408,0.04475)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.00925574179148701)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(0.082550753710271,0.050659467783408,0.01225)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148524,0.707046201633167,-0.00925574179148594,0.707046201633167)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(0.081700002890265,0.018170604721702,0.04475)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.00925574179148559,0.707046201633168,-0.00925574179148559,0.707046201633167)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(-0.081700002890277,0.018170604721702,0.04475)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

# Visualization shape 
body_9_11_shape = chrono.ChObjShapeFile() 
body_9_11_shape.SetFilename(shapes_dir +'body_9_11.obj') 
body_9_11_level = chrono.ChAssetLevel() 
body_9_11_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,-0.07033,0.04225)) 
body_9_11_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_11_level.GetAssets().push_back(body_9_11_shape) 
body_9.GetAssets().push_back(body_9_11_level) 

# Visualization shape 
body_9_191_shape = chrono.ChObjShapeFile() 
body_9_191_shape.SetFilename(shapes_dir +'body_9_191.obj') 
body_9_191_level = chrono.ChAssetLevel() 
body_9_191_level.GetFrame().SetPos(chrono.ChVectorD(-0.081700002890277,0.018170604721702,0.01225)) 
body_9_191_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707046201633167,0.009255741791487,-0.707046201633167,0.009255741791487)) 
body_9_191_level.GetAssets().push_back(body_9_191_shape) 
body_9.GetAssets().push_back(body_9_191_level) 

exported_items.append(body_9)



# Rigid body part
body_10= chrono.ChBodyAuxRef()
body_10.SetName('Upper Leg.step-3')
body_10.SetPos(chrono.ChVectorD(0.216874941702632,0.0868378597372417,0.250052088685122))
body_10.SetRot(chrono.ChQuaternionD(0.707106781186551,-0.707106781186544,1.1866149568071e-13,-1.17939171495601e-13))
body_10.SetMass(0.136105607367902)
body_10.SetInertiaXX(chrono.ChVectorD(0.00025112268751874,0.00027856514133726,4.3175169058668e-05))
body_10.SetInertiaXY(chrono.ChVectorD(1.42770165781856e-07,3.45711914261181e-06,-6.25406772913536e-06))
body_10.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.000248284196117477,0.0632516253278484,0.0012090578668991),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999939,0.00720000000000001)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_10.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_10.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_10.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_10.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_10.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_10.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,0.0072)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_10.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,-0.000549999999999939,-0.0071)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_10.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_10.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_10.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01105,0.03485,-0.0071)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_10.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_10_12_shape = chrono.ChObjShapeFile() 
body_10_12_shape.SetFilename(shapes_dir +'body_10_12.obj') 
body_10_12_level = chrono.ChAssetLevel() 
body_10_12_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_10_12_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_10_12_level.GetAssets().push_back(body_10_12_shape) 
body_10.GetAssets().push_back(body_10_12_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_10.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_10.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_10.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_10.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_10.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_10.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_10.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_10.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_10.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_10.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_10.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_10.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_10.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_10.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_10.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_10.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_10.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_10.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_10.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_10.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_10.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01545,0.01715,5.00000000000222E-05)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_10.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.05897405927155,0.0039)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_10.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,0.01255)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-3.53553390593269E-16,3.53553390593275E-16,0.707106781186547)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_10.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.10527029635775,0.0039)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_10.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02055,0.00700000585427701,5.01644618989966E-05)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-5.02028005945262E-30,0.707106781186547,5.02028005945262E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_10.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_39_shape = chrono.ChObjShapeFile() 
body_6_39_shape.SetFilename(shapes_dir +'body_6_39.obj') 
body_6_39_level = chrono.ChAssetLevel() 
body_6_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,0.14,-0.02)) 
body_6_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,3.53553390593269E-16,0.707106781186547,-3.53553390593269E-16)) 
body_6_39_level.GetAssets().push_back(body_6_39_shape) 
body_10.GetAssets().push_back(body_6_39_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.026097807647928,0.082122177814627,1.31943012071645E-10)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_10.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0,0.05897405927155,0.01255)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-3.53553390593269E-16,3.53553390593275E-16,0.707106781186547)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_10.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_42_shape = chrono.ChObjShapeFile() 
body_6_42_shape.SetFilename(shapes_dir +'body_6_42.obj') 
body_6_42_level = chrono.ChAssetLevel() 
body_6_42_level.GetFrame().SetPos(chrono.ChVectorD(0.02555,0.14,-0.02)) 
body_6_42_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186551,-3.74190954751083E-30,-8.79840521215611E-30,-0.707106781186544)) 
body_6_42_level.GetAssets().push_back(body_6_42_shape) 
body_10.GetAssets().push_back(body_6_42_level) 

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(0.0332,0.00700000585427704,5.01644618989966E-05)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-5.02028005945262E-30,0.707106781186547,5.02028005945262E-30)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_10.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_6_44_shape = chrono.ChObjShapeFile() 
body_6_44_shape.SetFilename(shapes_dir +'body_6_44.obj') 
body_6_44_level = chrono.ChAssetLevel() 
body_6_44_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_44_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_44_level.GetAssets().push_back(body_6_44_shape) 
body_10.GetAssets().push_back(body_6_44_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.017347807647928,0.082122177814627,1.31943012071645E-10)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-3.53553390593279E-16,-0.707106781186547,-3.53553390593279E-16)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_10.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_46_shape = chrono.ChObjShapeFile() 
body_6_46_shape.SetFilename(shapes_dir +'body_6_46.obj') 
body_6_46_level = chrono.ChAssetLevel() 
body_6_46_level.GetFrame().SetPos(chrono.ChVectorD(-0.02655,0.14811829320711,-0.022820012245991)) 
body_6_46_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,-0.5,0.5)) 
body_6_46_level.GetAssets().push_back(body_6_46_shape) 
body_10.GetAssets().push_back(body_6_46_level) 

# Visualization shape 
body_6_47_shape = chrono.ChObjShapeFile() 
body_6_47_shape.SetFilename(shapes_dir +'body_6_47.obj') 
body_6_47_level = chrono.ChAssetLevel() 
body_6_47_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_47_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_47_level.GetAssets().push_back(body_6_47_shape) 
body_10.GetAssets().push_back(body_6_47_level) 

exported_items.append(body_10)



# Rigid body part
body_11= chrono.ChBodyAuxRef()
body_11.SetName('RH Shoulder.step-1')
body_11.SetPos(chrono.ChVectorD(-0.0504079632019012,0.0855378597372699,0.46055208868513))
body_11.SetRot(chrono.ChQuaternionD(2.46885013108226e-15,2.46885013108227e-15,-0.707106781186546,0.707106781186549))
body_11.SetMass(0.118104660646891)
body_11.SetInertiaXX(chrono.ChVectorD(4.46841680139072e-05,0.000107948517541675,0.000120867442428233))
body_11.SetInertiaXY(chrono.ChVectorD(1.57611755382651e-05,1.1279955760135e-05,-2.22357650346175e-06))
body_11.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0425217629672545,-0.0165393982541154,-0.0134769683159427),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.031,-0.029065938370768)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_11.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_2_shape = chrono.ChObjShapeFile() 
body_5_2_shape.SetFilename(shapes_dir +'body_5_2.obj') 
body_5_2_level = chrono.ChAssetLevel() 
body_5_2_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.014463319489083,-0.03174508818529)) 
body_5_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_2_level.GetAssets().push_back(body_5_2_shape) 
body_11.GetAssets().push_back(body_5_2_level) 

# Visualization shape 
body_5_3_shape = chrono.ChObjShapeFile() 
body_5_3_shape.SetFilename(shapes_dir +'body_5_3.obj') 
body_5_3_level = chrono.ChAssetLevel() 
body_5_3_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.04515,1.49991130626859E-13)) 
body_5_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,0.5,0.5,0.5)) 
body_5_3_level.GetAssets().push_back(body_5_3_shape) 
body_11.GetAssets().push_back(body_5_3_level) 

# Visualization shape 
body_5_4_shape = chrono.ChObjShapeFile() 
body_5_4_shape.SetFilename(shapes_dir +'body_5_4.obj') 
body_5_4_level = chrono.ChAssetLevel() 
body_5_4_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_4_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_4_level.GetAssets().push_back(body_5_4_shape) 
body_11.GetAssets().push_back(body_5_4_level) 

# Visualization shape 
body_5_5_shape = chrono.ChObjShapeFile() 
body_5_5_shape.SetFilename(shapes_dir +'body_5_5.obj') 
body_5_5_level = chrono.ChAssetLevel() 
body_5_5_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_5_level.GetAssets().push_back(body_5_5_shape) 
body_11.GetAssets().push_back(body_5_5_level) 

# Visualization shape 
body_5_6_shape = chrono.ChObjShapeFile() 
body_5_6_shape.SetFilename(shapes_dir +'body_5_6.obj') 
body_5_6_level = chrono.ChAssetLevel() 
body_5_6_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_6_level.GetAssets().push_back(body_5_6_shape) 
body_11.GetAssets().push_back(body_5_6_level) 

# Visualization shape 
body_5_7_shape = chrono.ChObjShapeFile() 
body_5_7_shape.SetFilename(shapes_dir +'body_5_7.obj') 
body_5_7_level = chrono.ChAssetLevel() 
body_5_7_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_7_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_7_level.GetAssets().push_back(body_5_7_shape) 
body_11.GetAssets().push_back(body_5_7_level) 

# Visualization shape 
body_5_8_shape = chrono.ChObjShapeFile() 
body_5_8_shape.SetFilename(shapes_dir +'body_5_8.obj') 
body_5_8_level = chrono.ChAssetLevel() 
body_5_8_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_8_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_8_level.GetAssets().push_back(body_5_8_shape) 
body_11.GetAssets().push_back(body_5_8_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845224,-0.0231,-0.0278499999998581)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_11.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_11_10_shape = chrono.ChObjShapeFile() 
body_11_10_shape.SetFilename(shapes_dir +'body_11_10.obj') 
body_11_10_level = chrono.ChAssetLevel() 
body_11_10_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_11_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_11_10_level.GetAssets().push_back(body_11_10_shape) 
body_11.GetAssets().push_back(body_11_10_level) 

# Visualization shape 
body_5_11_shape = chrono.ChObjShapeFile() 
body_5_11_shape.SetFilename(shapes_dir +'body_5_11.obj') 
body_5_11_level = chrono.ChAssetLevel() 
body_5_11_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_11_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_11_level.GetAssets().push_back(body_5_11_shape) 
body_11.GetAssets().push_back(body_5_11_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845224,-0.0231,-0.0278499999998588)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_11.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_13_shape = chrono.ChObjShapeFile() 
body_5_13_shape.SetFilename(shapes_dir +'body_5_13.obj') 
body_5_13_level = chrono.ChAssetLevel() 
body_5_13_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_13_level.GetAssets().push_back(body_5_13_shape) 
body_11.GetAssets().push_back(body_5_13_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845226,-0.0231,0.00755000000014186)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_11.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_15_shape = chrono.ChObjShapeFile() 
body_5_15_shape.SetFilename(shapes_dir +'body_5_15.obj') 
body_5_15_level = chrono.ChAssetLevel() 
body_5_15_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_15_level.GetAssets().push_back(body_5_15_shape) 
body_11.GetAssets().push_back(body_5_15_level) 

# Visualization shape 
body_5_16_shape = chrono.ChObjShapeFile() 
body_5_16_shape.SetFilename(shapes_dir +'body_5_16.obj') 
body_5_16_level = chrono.ChAssetLevel() 
body_5_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_16_level.GetAssets().push_back(body_5_16_shape) 
body_11.GetAssets().push_back(body_5_16_level) 

# Visualization shape 
body_5_17_shape = chrono.ChObjShapeFile() 
body_5_17_shape.SetFilename(shapes_dir +'body_5_17.obj') 
body_5_17_level = chrono.ChAssetLevel() 
body_5_17_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_17_level.GetAssets().push_back(body_5_17_shape) 
body_11.GetAssets().push_back(body_5_17_level) 

# Visualization shape 
body_5_18_shape = chrono.ChObjShapeFile() 
body_5_18_shape.SetFilename(shapes_dir +'body_5_18.obj') 
body_5_18_level = chrono.ChAssetLevel() 
body_5_18_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_18_level.GetAssets().push_back(body_5_18_shape) 
body_11.GetAssets().push_back(body_5_18_level) 

# Visualization shape 
body_5_19_shape = chrono.ChObjShapeFile() 
body_5_19_shape.SetFilename(shapes_dir +'body_5_19.obj') 
body_5_19_level = chrono.ChAssetLevel() 
body_5_19_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_19_level.GetAssets().push_back(body_5_19_shape) 
body_11.GetAssets().push_back(body_5_19_level) 

# Visualization shape 
body_5_20_shape = chrono.ChObjShapeFile() 
body_5_20_shape.SetFilename(shapes_dir +'body_5_20.obj') 
body_5_20_level = chrono.ChAssetLevel() 
body_5_20_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_20_level.GetAssets().push_back(body_5_20_shape) 
body_11.GetAssets().push_back(body_5_20_level) 

# Visualization shape 
body_5_21_shape = chrono.ChObjShapeFile() 
body_5_21_shape.SetFilename(shapes_dir +'body_5_21.obj') 
body_5_21_level = chrono.ChAssetLevel() 
body_5_21_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_21_level.GetAssets().push_back(body_5_21_shape) 
body_11.GetAssets().push_back(body_5_21_level) 

# Visualization shape 
body_5_9_shape = chrono.ChObjShapeFile() 
body_5_9_shape.SetFilename(shapes_dir +'body_5_9.obj') 
body_5_9_level = chrono.ChAssetLevel() 
body_5_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845226,-0.0231,0.00755000000014115)) 
body_5_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)) 
body_5_9_level.GetAssets().push_back(body_5_9_shape) 
body_11.GetAssets().push_back(body_5_9_level) 

# Visualization shape 
body_5_23_shape = chrono.ChObjShapeFile() 
body_5_23_shape.SetFilename(shapes_dir +'body_5_23.obj') 
body_5_23_level = chrono.ChAssetLevel() 
body_5_23_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_23_level.GetAssets().push_back(body_5_23_shape) 
body_11.GetAssets().push_back(body_5_23_level) 

# Visualization shape 
body_5_24_shape = chrono.ChObjShapeFile() 
body_5_24_shape.SetFilename(shapes_dir +'body_5_24.obj') 
body_5_24_level = chrono.ChAssetLevel() 
body_5_24_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_24_level.GetAssets().push_back(body_5_24_shape) 
body_11.GetAssets().push_back(body_5_24_level) 

# Visualization shape 
body_5_25_shape = chrono.ChObjShapeFile() 
body_5_25_shape.SetFilename(shapes_dir +'body_5_25.obj') 
body_5_25_level = chrono.ChAssetLevel() 
body_5_25_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_25_level.GetAssets().push_back(body_5_25_shape) 
body_11.GetAssets().push_back(body_5_25_level) 

# Visualization shape 
body_5_26_shape = chrono.ChObjShapeFile() 
body_5_26_shape.SetFilename(shapes_dir +'body_5_26.obj') 
body_5_26_level = chrono.ChAssetLevel() 
body_5_26_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_26_level.GetAssets().push_back(body_5_26_shape) 
body_11.GetAssets().push_back(body_5_26_level) 

# Visualization shape 
body_5_27_shape = chrono.ChObjShapeFile() 
body_5_27_shape.SetFilename(shapes_dir +'body_5_27.obj') 
body_5_27_level = chrono.ChAssetLevel() 
body_5_27_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_27_level.GetAssets().push_back(body_5_27_shape) 
body_11.GetAssets().push_back(body_5_27_level) 

# Visualization shape 
body_5_28_shape = chrono.ChObjShapeFile() 
body_5_28_shape.SetFilename(shapes_dir +'body_5_28.obj') 
body_5_28_level = chrono.ChAssetLevel() 
body_5_28_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_28_level.GetAssets().push_back(body_5_28_shape) 
body_11.GetAssets().push_back(body_5_28_level) 

# Visualization shape 
body_5_29_shape = chrono.ChObjShapeFile() 
body_5_29_shape.SetFilename(shapes_dir +'body_5_29.obj') 
body_5_29_level = chrono.ChAssetLevel() 
body_5_29_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_29_level.GetAssets().push_back(body_5_29_shape) 
body_11.GetAssets().push_back(body_5_29_level) 

# Visualization shape 
body_5_30_shape = chrono.ChObjShapeFile() 
body_5_30_shape.SetFilename(shapes_dir +'body_5_30.obj') 
body_5_30_level = chrono.ChAssetLevel() 
body_5_30_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_30_level.GetAssets().push_back(body_5_30_shape) 
body_11.GetAssets().push_back(body_5_30_level) 

# Visualization shape 
body_5_31_shape = chrono.ChObjShapeFile() 
body_5_31_shape.SetFilename(shapes_dir +'body_5_31.obj') 
body_5_31_level = chrono.ChAssetLevel() 
body_5_31_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_31_level.GetAssets().push_back(body_5_31_shape) 
body_11.GetAssets().push_back(body_5_31_level) 

# Visualization shape 
body_5_32_shape = chrono.ChObjShapeFile() 
body_5_32_shape.SetFilename(shapes_dir +'body_5_32.obj') 
body_5_32_level = chrono.ChAssetLevel() 
body_5_32_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_32_level.GetAssets().push_back(body_5_32_shape) 
body_11.GetAssets().push_back(body_5_32_level) 

# Visualization shape 
body_5_33_shape = chrono.ChObjShapeFile() 
body_5_33_shape.SetFilename(shapes_dir +'body_5_33.obj') 
body_5_33_level = chrono.ChAssetLevel() 
body_5_33_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_33_level.GetAssets().push_back(body_5_33_shape) 
body_11.GetAssets().push_back(body_5_33_level) 

# Visualization shape 
body_5_34_shape = chrono.ChObjShapeFile() 
body_5_34_shape.SetFilename(shapes_dir +'body_5_34.obj') 
body_5_34_level = chrono.ChAssetLevel() 
body_5_34_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_34_level.GetAssets().push_back(body_5_34_shape) 
body_11.GetAssets().push_back(body_5_34_level) 

# Visualization shape 
body_5_35_shape = chrono.ChObjShapeFile() 
body_5_35_shape.SetFilename(shapes_dir +'body_5_35.obj') 
body_5_35_level = chrono.ChAssetLevel() 
body_5_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_35_level.GetAssets().push_back(body_5_35_shape) 
body_11.GetAssets().push_back(body_5_35_level) 

# Visualization shape 
body_5_36_shape = chrono.ChObjShapeFile() 
body_5_36_shape.SetFilename(shapes_dir +'body_5_36.obj') 
body_5_36_level = chrono.ChAssetLevel() 
body_5_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_36_level.GetAssets().push_back(body_5_36_shape) 
body_11.GetAssets().push_back(body_5_36_level) 

# Visualization shape 
body_5_37_shape = chrono.ChObjShapeFile() 
body_5_37_shape.SetFilename(shapes_dir +'body_5_37.obj') 
body_5_37_level = chrono.ChAssetLevel() 
body_5_37_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_37_level.GetAssets().push_back(body_5_37_shape) 
body_11.GetAssets().push_back(body_5_37_level) 

# Visualization shape 
body_5_38_shape = chrono.ChObjShapeFile() 
body_5_38_shape.SetFilename(shapes_dir +'body_5_38.obj') 
body_5_38_level = chrono.ChAssetLevel() 
body_5_38_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,-0.010149999999857)) 
body_5_38_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999995,0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_5_38_level.GetAssets().push_back(body_5_38_shape) 
body_11.GetAssets().push_back(body_5_38_level) 

# Visualization shape 
body_5_39_shape = chrono.ChObjShapeFile() 
body_5_39_shape.SetFilename(shapes_dir +'body_5_39.obj') 
body_5_39_level = chrono.ChAssetLevel() 
body_5_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02955,-0.018,-0.00120000000000101)) 
body_5_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_39_level.GetAssets().push_back(body_5_39_shape) 
body_11.GetAssets().push_back(body_5_39_level) 

# Visualization shape 
body_5_40_shape = chrono.ChObjShapeFile() 
body_5_40_shape.SetFilename(shapes_dir +'body_5_40.obj') 
body_5_40_level = chrono.ChAssetLevel() 
body_5_40_level.GetFrame().SetPos(chrono.ChVectorD(-0.02955,-0.020820012245991,0.00691829320710799)) 
body_5_40_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,0,-0.707106781186547)) 
body_5_40_level.GetAssets().push_back(body_5_40_shape) 
body_11.GetAssets().push_back(body_5_40_level) 

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.032,1.50005008414666E-13)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999997,0.500000000000003,0.499999999999997,0.500000000000003)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_11.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.014463319489083,-0.03174508818529)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_11.GetAssets().push_back(body_5_1_level) 

# Visualization shape 
body_5_2_shape = chrono.ChObjShapeFile() 
body_5_2_shape.SetFilename(shapes_dir +'body_5_2.obj') 
body_5_2_level = chrono.ChAssetLevel() 
body_5_2_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.031,-0.029065938370768)) 
body_5_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0)) 
body_5_2_level.GetAssets().push_back(body_5_2_shape) 
body_11.GetAssets().push_back(body_5_2_level) 

# Visualization shape 
body_5_44_shape = chrono.ChObjShapeFile() 
body_5_44_shape.SetFilename(shapes_dir +'body_5_44.obj') 
body_5_44_level = chrono.ChAssetLevel() 
body_5_44_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,-0.018,-0.00120000000000101)) 
body_5_44_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186546,0,0,-0.707106781186549)) 
body_5_44_level.GetAssets().push_back(body_5_44_shape) 
body_11.GetAssets().push_back(body_5_44_level) 

# Visualization shape 
body_5_45_shape = chrono.ChObjShapeFile() 
body_5_45_shape.SetFilename(shapes_dir +'body_5_45.obj') 
body_5_45_level = chrono.ChAssetLevel() 
body_5_45_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_45_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_45_level.GetAssets().push_back(body_5_45_shape) 
body_11.GetAssets().push_back(body_5_45_level) 

exported_items.append(body_11)



# Rigid body part
body_12= chrono.ChBodyAuxRef()
body_12.SetName('LH Shoulder.step-1')
body_12.SetPos(chrono.ChVectorD(0.216874941702632,0.085537859737271,0.460552088685129))
body_12.SetRot(chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,-2.38111134520566e-15,2.44937623471364e-15))
body_12.SetMass(0.118103187382885)
body_12.SetInertiaXX(chrono.ChVectorD(4.46830780759277e-05,0.000107946537422069,0.00012086601634151))
body_12.SetInertiaXY(chrono.ChVectorD(1.57606503508095e-05,1.12790186398685e-05,-2.22311335801096e-06))
body_12.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0425214406592162,-0.0165396904773734,0.0134771264279906),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.0451499999999999,-1.49991130626859E-13)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_12.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.031,0.029065938370768)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,4.74573349370131E-30,0.707106781186548,-4.7370177297092E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_12.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084522,-0.0319999999999999,-1.49991130626859E-13)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.499999999999997,0.500000000000003,0.499999999999997,-0.500000000000003)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_12.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.014463319489083,0.03174508818529)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,4.74573349370131E-30,0.707106781186548,-4.7370177297092E-30)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_12.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845227,-0.0231,-0.00755000000014315)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,-0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_12.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_12.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_12.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_12.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_12.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_12.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0748851890845234,-0.0231,0.0278499999998569)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,-0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_12.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845227,-0.0231,-0.00755000000014285)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,-0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_12.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_12.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_12.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.0605851890845234,-0.0231,0.0278499999998572)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,-0.499999999999995,0.500000000000005,-0.500000000000005)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_12.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_12_16_shape = chrono.ChObjShapeFile() 
body_12_16_shape.SetFilename(shapes_dir +'body_12_16.obj') 
body_12_16_level = chrono.ChAssetLevel() 
body_12_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_12_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_12_16_level.GetAssets().push_back(body_12_16_shape) 
body_12.GetAssets().push_back(body_12_16_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_12.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_12.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_12.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_12.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_12.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_12.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_12.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_12.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_12.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_12.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_12.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_12.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_12.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_12.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_12.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_12.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_12.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_12.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_12.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_12.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_12.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(-0.067735189084523,-0.0275,0.010149999999857)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.499999999999995,0.499999999999995,0.500000000000005,0.500000000000005)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_12.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_7_39_shape = chrono.ChObjShapeFile() 
body_7_39_shape.SetFilename(shapes_dir +'body_7_39.obj') 
body_7_39_level = chrono.ChAssetLevel() 
body_7_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_39_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_39_level.GetAssets().push_back(body_7_39_shape) 
body_12.GetAssets().push_back(body_7_39_level) 

# Visualization shape 
body_7_40_shape = chrono.ChObjShapeFile() 
body_7_40_shape.SetFilename(shapes_dir +'body_7_40.obj') 
body_7_40_level = chrono.ChAssetLevel() 
body_7_40_level.GetFrame().SetPos(chrono.ChVectorD(-0.02955,-0.0208200122459909,-0.00691829320710799)) 
body_7_40_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-4.90487860999068E-30,4.57787261341983E-30,-0.707106781186547)) 
body_7_40_level.GetAssets().push_back(body_7_40_shape) 
body_12.GetAssets().push_back(body_7_40_level) 

# Visualization shape 
body_6_39_shape = chrono.ChObjShapeFile() 
body_6_39_shape.SetFilename(shapes_dir +'body_6_39.obj') 
body_6_39_level = chrono.ChAssetLevel() 
body_6_39_level.GetFrame().SetPos(chrono.ChVectorD(0.02955,-0.018,0.00120000000000101)) 
body_6_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,4.74573349370131E-30,0.707106781186548,-4.7370177297092E-30)) 
body_6_39_level.GetAssets().push_back(body_6_39_shape) 
body_12.GetAssets().push_back(body_6_39_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.02355,-0.014463319489083,0.03174508818529)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,4.74573349370131E-30,0.707106781186548,-4.7370177297092E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_12.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.0312,-0.031,0.029065938370768)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,4.74573349370131E-30,0.707106781186548,-4.7370177297092E-30)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_12.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_7_44_shape = chrono.ChObjShapeFile() 
body_7_44_shape.SetFilename(shapes_dir +'body_7_44.obj') 
body_7_44_level = chrono.ChAssetLevel() 
body_7_44_level.GetFrame().SetPos(chrono.ChVectorD(0.02755,-0.018,0.00120000000000101)) 
body_7_44_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186546,-4.86520207035907E-30,4.57787261341983E-30,-0.707106781186548)) 
body_7_44_level.GetAssets().push_back(body_7_44_shape) 
body_12.GetAssets().push_back(body_7_44_level) 

# Visualization shape 
body_7_45_shape = chrono.ChObjShapeFile() 
body_7_45_shape.SetFilename(shapes_dir +'body_7_45.obj') 
body_7_45_level = chrono.ChAssetLevel() 
body_7_45_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_45_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_45_level.GetAssets().push_back(body_7_45_shape) 
body_12.GetAssets().push_back(body_7_45_level) 

exported_items.append(body_12)



# Rigid body part
body_13= chrono.ChBodyAuxRef()
body_13.SetName('Lower Leg.step-1')
body_13.SetPos(chrono.ChVectorD(0.216874941702632,0.0867378597372723,0.485552088685129))
body_13.SetRot(chrono.ChQuaternionD(0.707106781186551,-0.707106781186544,-2.2854338360046e-15,2.35369872551262e-15))
body_13.SetMass(0.0965195912663027)
body_13.SetInertiaXX(chrono.ChVectorD(0.000185078635413758,0.000191942424654836,1.37684925494417e-05))
body_13.SetInertiaXY(chrono.ChVectorD(8.37154460649505e-09,-1.85165490763447e-06,-5.63860607834635e-07))
body_13.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000646606827372261,0.0946701125929855,-0.0216225845247406),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_13.GetAssets().push_back(body_8_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,-0.0272)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_13.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_13.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_13.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_13.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_13.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_13.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,-0.0272)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_13.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.14755,-0.0129)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_13.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_13.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_13.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.01305,0.11215,-0.0129)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_13.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_13_13_shape = chrono.ChObjShapeFile() 
body_13_13_shape.SetFilename(shapes_dir +'body_13_13.obj') 
body_13_13_level = chrono.ChAssetLevel() 
body_13_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_13_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_13_13_level.GetAssets().push_back(body_13_13_shape) 
body_13.GetAssets().push_back(body_13_13_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_13.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_13.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_13.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_13.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_13.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_13.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_13.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_13.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_13.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_13.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_13.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_13.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_13.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_13.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_13.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_13.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_13.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_13.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_13.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_13.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_13.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(0.01745,0.12985,-0.02005)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,-0.5)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_13.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.01855,0.140000131576897,-0.020050271710659)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,-1.0851126170171E-30,0.707106781186548,1.14612296496184E-30)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_13.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_43_shape = chrono.ChObjShapeFile() 
body_6_43_shape.SetFilename(shapes_dir +'body_6_43.obj') 
body_6_43_level = chrono.ChAssetLevel() 
body_6_43_level.GetFrame().SetPos(chrono.ChVectorD(0.0302,0.140000131576897,-0.020050271710659)) 
body_6_43_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186547,-1.0851126170171E-30,0.707106781186548,1.14612296496184E-30)) 
body_6_43_level.GetAssets().push_back(body_6_43_shape) 
body_13.GetAssets().push_back(body_6_43_level) 

# Visualization shape 
body_8_38_shape = chrono.ChObjShapeFile() 
body_8_38_shape.SetFilename(shapes_dir +'body_8_38.obj') 
body_8_38_level = chrono.ChAssetLevel() 
body_8_38_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_38_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_38_level.GetAssets().push_back(body_8_38_shape) 
body_13.GetAssets().push_back(body_8_38_level) 

exported_items.append(body_13)



# Rigid body part
body_14= chrono.ChBodyAuxRef()
body_14.SetName('Head.step-1')
body_14.SetPos(chrono.ChVectorD(0.0832334892503635,0.0703324589092862,0.298052088685129))
body_14.SetRot(chrono.ChQuaternionD(-2.46803298682877e-15,-2.46794518015835e-15,0.707106781186549,0.707106781186546))
body_14.SetMass(0.489895287630459)
body_14.SetInertiaXX(chrono.ChVectorD(0.000961176486146265,0.00186141095225632,0.00141012004620865))
body_14.SetInertiaXY(chrono.ChVectorD(2.34226143004007e-06,1.1519890002003e-05,9.82383076890466e-06))
body_14.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.000691398345654931,0.185021062650433,0.0335749335310775),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.1896,0.026)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-1.62904077916488E-32,-1.65979828973108E-32)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.00714999999999999,0.1691,0.0186)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_14.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_2_shape = chrono.ChObjShapeFile() 
body_6_2_shape.SetFilename(shapes_dir +'body_6_2.obj') 
body_6_2_level = chrono.ChAssetLevel() 
body_6_2_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_2_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_2_level.GetAssets().push_back(body_6_2_shape) 
body_14.GetAssets().push_back(body_6_2_level) 

# Visualization shape 
body_6_3_shape = chrono.ChObjShapeFile() 
body_6_3_shape.SetFilename(shapes_dir +'body_6_3.obj') 
body_6_3_level = chrono.ChAssetLevel() 
body_6_3_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_3_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_3_level.GetAssets().push_back(body_6_3_shape) 
body_14.GetAssets().push_back(body_6_3_level) 

# Visualization shape 
body_6_4_shape = chrono.ChObjShapeFile() 
body_6_4_shape.SetFilename(shapes_dir +'body_6_4.obj') 
body_6_4_level = chrono.ChAssetLevel() 
body_6_4_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_4_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_4_level.GetAssets().push_back(body_6_4_shape) 
body_14.GetAssets().push_back(body_6_4_level) 

# Visualization shape 
body_6_5_shape = chrono.ChObjShapeFile() 
body_6_5_shape.SetFilename(shapes_dir +'body_6_5.obj') 
body_6_5_level = chrono.ChAssetLevel() 
body_6_5_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_5_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_5_level.GetAssets().push_back(body_6_5_shape) 
body_14.GetAssets().push_back(body_6_5_level) 

# Visualization shape 
body_6_6_shape = chrono.ChObjShapeFile() 
body_6_6_shape.SetFilename(shapes_dir +'body_6_6.obj') 
body_6_6_level = chrono.ChAssetLevel() 
body_6_6_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_6_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_6_level.GetAssets().push_back(body_6_6_shape) 
body_14.GetAssets().push_back(body_6_6_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0.00714999999999999,0.1691,0.054)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_14.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.00715000000000002,0.1691,0.0186)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_14.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_6_9_shape = chrono.ChObjShapeFile() 
body_6_9_shape.SetFilename(shapes_dir +'body_6_9.obj') 
body_6_9_level = chrono.ChAssetLevel() 
body_6_9_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_9_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_9_level.GetAssets().push_back(body_6_9_shape) 
body_14.GetAssets().push_back(body_6_9_level) 

# Visualization shape 
body_6_10_shape = chrono.ChObjShapeFile() 
body_6_10_shape.SetFilename(shapes_dir +'body_6_10.obj') 
body_6_10_level = chrono.ChAssetLevel() 
body_6_10_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_10_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_10_level.GetAssets().push_back(body_6_10_shape) 
body_14.GetAssets().push_back(body_6_10_level) 

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(-0.00715000000000002,0.1691,0.054)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_14.GetAssets().push_back(body_6_1_level) 

# Visualization shape 
body_14_13_shape = chrono.ChObjShapeFile() 
body_14_13_shape.SetFilename(shapes_dir +'body_14_13.obj') 
body_14_13_level = chrono.ChAssetLevel() 
body_14_13_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_14_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_14_13_level.GetAssets().push_back(body_14_13_shape) 
body_14.GetAssets().push_back(body_14_13_level) 

# Visualization shape 
body_6_13_shape = chrono.ChObjShapeFile() 
body_6_13_shape.SetFilename(shapes_dir +'body_6_13.obj') 
body_6_13_level = chrono.ChAssetLevel() 
body_6_13_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_13_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_13_level.GetAssets().push_back(body_6_13_shape) 
body_14.GetAssets().push_back(body_6_13_level) 

# Visualization shape 
body_6_14_shape = chrono.ChObjShapeFile() 
body_6_14_shape.SetFilename(shapes_dir +'body_6_14.obj') 
body_6_14_level = chrono.ChAssetLevel() 
body_6_14_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_14_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_14_level.GetAssets().push_back(body_6_14_shape) 
body_14.GetAssets().push_back(body_6_14_level) 

# Visualization shape 
body_6_15_shape = chrono.ChObjShapeFile() 
body_6_15_shape.SetFilename(shapes_dir +'body_6_15.obj') 
body_6_15_level = chrono.ChAssetLevel() 
body_6_15_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_15_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_15_level.GetAssets().push_back(body_6_15_shape) 
body_14.GetAssets().push_back(body_6_15_level) 

# Visualization shape 
body_6_16_shape = chrono.ChObjShapeFile() 
body_6_16_shape.SetFilename(shapes_dir +'body_6_16.obj') 
body_6_16_level = chrono.ChAssetLevel() 
body_6_16_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_16_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_16_level.GetAssets().push_back(body_6_16_shape) 
body_14.GetAssets().push_back(body_6_16_level) 

# Visualization shape 
body_6_17_shape = chrono.ChObjShapeFile() 
body_6_17_shape.SetFilename(shapes_dir +'body_6_17.obj') 
body_6_17_level = chrono.ChAssetLevel() 
body_6_17_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_17_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_17_level.GetAssets().push_back(body_6_17_shape) 
body_14.GetAssets().push_back(body_6_17_level) 

# Visualization shape 
body_6_18_shape = chrono.ChObjShapeFile() 
body_6_18_shape.SetFilename(shapes_dir +'body_6_18.obj') 
body_6_18_level = chrono.ChAssetLevel() 
body_6_18_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_18_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_18_level.GetAssets().push_back(body_6_18_shape) 
body_14.GetAssets().push_back(body_6_18_level) 

# Visualization shape 
body_6_19_shape = chrono.ChObjShapeFile() 
body_6_19_shape.SetFilename(shapes_dir +'body_6_19.obj') 
body_6_19_level = chrono.ChAssetLevel() 
body_6_19_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_19_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_19_level.GetAssets().push_back(body_6_19_shape) 
body_14.GetAssets().push_back(body_6_19_level) 

# Visualization shape 
body_6_20_shape = chrono.ChObjShapeFile() 
body_6_20_shape.SetFilename(shapes_dir +'body_6_20.obj') 
body_6_20_level = chrono.ChAssetLevel() 
body_6_20_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_20_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_20_level.GetAssets().push_back(body_6_20_shape) 
body_14.GetAssets().push_back(body_6_20_level) 

# Visualization shape 
body_6_21_shape = chrono.ChObjShapeFile() 
body_6_21_shape.SetFilename(shapes_dir +'body_6_21.obj') 
body_6_21_level = chrono.ChAssetLevel() 
body_6_21_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_21_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_21_level.GetAssets().push_back(body_6_21_shape) 
body_14.GetAssets().push_back(body_6_21_level) 

# Visualization shape 
body_6_22_shape = chrono.ChObjShapeFile() 
body_6_22_shape.SetFilename(shapes_dir +'body_6_22.obj') 
body_6_22_level = chrono.ChAssetLevel() 
body_6_22_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_22_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_22_level.GetAssets().push_back(body_6_22_shape) 
body_14.GetAssets().push_back(body_6_22_level) 

# Visualization shape 
body_6_23_shape = chrono.ChObjShapeFile() 
body_6_23_shape.SetFilename(shapes_dir +'body_6_23.obj') 
body_6_23_level = chrono.ChAssetLevel() 
body_6_23_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_23_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_23_level.GetAssets().push_back(body_6_23_shape) 
body_14.GetAssets().push_back(body_6_23_level) 

# Visualization shape 
body_6_24_shape = chrono.ChObjShapeFile() 
body_6_24_shape.SetFilename(shapes_dir +'body_6_24.obj') 
body_6_24_level = chrono.ChAssetLevel() 
body_6_24_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_24_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_24_level.GetAssets().push_back(body_6_24_shape) 
body_14.GetAssets().push_back(body_6_24_level) 

# Visualization shape 
body_6_25_shape = chrono.ChObjShapeFile() 
body_6_25_shape.SetFilename(shapes_dir +'body_6_25.obj') 
body_6_25_level = chrono.ChAssetLevel() 
body_6_25_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_25_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_25_level.GetAssets().push_back(body_6_25_shape) 
body_14.GetAssets().push_back(body_6_25_level) 

# Visualization shape 
body_6_26_shape = chrono.ChObjShapeFile() 
body_6_26_shape.SetFilename(shapes_dir +'body_6_26.obj') 
body_6_26_level = chrono.ChAssetLevel() 
body_6_26_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_26_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_26_level.GetAssets().push_back(body_6_26_shape) 
body_14.GetAssets().push_back(body_6_26_level) 

# Visualization shape 
body_6_27_shape = chrono.ChObjShapeFile() 
body_6_27_shape.SetFilename(shapes_dir +'body_6_27.obj') 
body_6_27_level = chrono.ChAssetLevel() 
body_6_27_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_27_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_27_level.GetAssets().push_back(body_6_27_shape) 
body_14.GetAssets().push_back(body_6_27_level) 

# Visualization shape 
body_6_28_shape = chrono.ChObjShapeFile() 
body_6_28_shape.SetFilename(shapes_dir +'body_6_28.obj') 
body_6_28_level = chrono.ChAssetLevel() 
body_6_28_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_28_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_28_level.GetAssets().push_back(body_6_28_shape) 
body_14.GetAssets().push_back(body_6_28_level) 

# Visualization shape 
body_6_29_shape = chrono.ChObjShapeFile() 
body_6_29_shape.SetFilename(shapes_dir +'body_6_29.obj') 
body_6_29_level = chrono.ChAssetLevel() 
body_6_29_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_29_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_29_level.GetAssets().push_back(body_6_29_shape) 
body_14.GetAssets().push_back(body_6_29_level) 

# Visualization shape 
body_6_30_shape = chrono.ChObjShapeFile() 
body_6_30_shape.SetFilename(shapes_dir +'body_6_30.obj') 
body_6_30_level = chrono.ChAssetLevel() 
body_6_30_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_30_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_30_level.GetAssets().push_back(body_6_30_shape) 
body_14.GetAssets().push_back(body_6_30_level) 

# Visualization shape 
body_6_31_shape = chrono.ChObjShapeFile() 
body_6_31_shape.SetFilename(shapes_dir +'body_6_31.obj') 
body_6_31_level = chrono.ChAssetLevel() 
body_6_31_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_31_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_31_level.GetAssets().push_back(body_6_31_shape) 
body_14.GetAssets().push_back(body_6_31_level) 

# Visualization shape 
body_6_32_shape = chrono.ChObjShapeFile() 
body_6_32_shape.SetFilename(shapes_dir +'body_6_32.obj') 
body_6_32_level = chrono.ChAssetLevel() 
body_6_32_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_32_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_32_level.GetAssets().push_back(body_6_32_shape) 
body_14.GetAssets().push_back(body_6_32_level) 

# Visualization shape 
body_6_33_shape = chrono.ChObjShapeFile() 
body_6_33_shape.SetFilename(shapes_dir +'body_6_33.obj') 
body_6_33_level = chrono.ChAssetLevel() 
body_6_33_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_33_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_33_level.GetAssets().push_back(body_6_33_shape) 
body_14.GetAssets().push_back(body_6_33_level) 

# Visualization shape 
body_6_34_shape = chrono.ChObjShapeFile() 
body_6_34_shape.SetFilename(shapes_dir +'body_6_34.obj') 
body_6_34_level = chrono.ChAssetLevel() 
body_6_34_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.1735,0.0363)) 
body_6_34_level.GetFrame().SetRot(chrono.ChQuaternionD(-0.5,-0.5,0.5,-0.5)) 
body_6_34_level.GetAssets().push_back(body_6_34_shape) 
body_14.GetAssets().push_back(body_6_34_level) 

# Visualization shape 
body_14_36_shape = chrono.ChObjShapeFile() 
body_14_36_shape.SetFilename(shapes_dir +'body_14_36.obj') 
body_14_36_level = chrono.ChAssetLevel() 
body_14_36_level.GetFrame().SetPos(chrono.ChVectorD(-1.99840144432528E-15,0.224293172785605,0.037201866975123)) 
body_14_36_level.GetFrame().SetRot(chrono.ChQuaternionD(0.99144486137381,-0.130526192220052,-5.52370871100746E-33,1.18738290385152E-32)) 
body_14_36_level.GetAssets().push_back(body_14_36_shape) 
body_14.GetAssets().push_back(body_14_36_level) 

# Visualization shape 
body_14_37_shape = chrono.ChObjShapeFile() 
body_14_37_shape.SetFilename(shapes_dir +'body_14_37.obj') 
body_14_37_level = chrono.ChAssetLevel() 
body_14_37_level.GetFrame().SetPos(chrono.ChVectorD(-1.38777878078145E-17,0.245170856323837,0.040148737019605)) 
body_14_37_level.GetFrame().SetRot(chrono.ChQuaternionD(0.608761429008721,-0.793353340291235,-3.82502651484943E-32,-2.83224036198357E-32)) 
body_14_37_level.GetAssets().push_back(body_14_37_shape) 
body_14.GetAssets().push_back(body_14_37_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0,0.1741,0.026)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-1.62904077916488E-32,-1.65979828973108E-32)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_14_39_shape = chrono.ChObjShapeFile() 
body_14_39_shape.SetFilename(shapes_dir +'body_14_39.obj') 
body_14_39_level = chrono.ChAssetLevel() 
body_14_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0.19525,0.026)) 
body_14_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-1.62904077916488E-32,-1.65979828973108E-32)) 
body_14_39_level.GetAssets().push_back(body_14_39_shape) 
body_14.GetAssets().push_back(body_14_39_level) 

# Visualization shape 
body_6_39_shape = chrono.ChObjShapeFile() 
body_6_39_shape.SetFilename(shapes_dir +'body_6_39.obj') 
body_6_39_level = chrono.ChAssetLevel() 
body_6_39_level.GetFrame().SetPos(chrono.ChVectorD(0,0.1831,0.026)) 
body_6_39_level.GetFrame().SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-1.62904077916488E-32,-1.65979828973108E-32)) 
body_6_39_level.GetAssets().push_back(body_6_39_shape) 
body_14.GetAssets().push_back(body_6_39_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.085188180946079,0.139000000000001,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(0.082175575885391,0.208000000000001,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.085188180946079,0.139000000000001,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_35_shape = chrono.ChObjShapeFile() 
body_6_35_shape.SetFilename(shapes_dir +'body_6_35.obj') 
body_6_35_level = chrono.ChAssetLevel() 
body_6_35_level.GetFrame().SetPos(chrono.ChVectorD(-0.082175575885392,0.208000000000001,0.048)) 
body_6_35_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_35_level.GetAssets().push_back(body_6_35_shape) 
body_14.GetAssets().push_back(body_6_35_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.082175575885391,0.208000000000001,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_14.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(-0.085188180946079,0.139000000000001,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_14.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_14_47_shape = chrono.ChObjShapeFile() 
body_14_47_shape.SetFilename(shapes_dir +'body_14_47.obj') 
body_14_47_level = chrono.ChAssetLevel() 
body_14_47_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_14_47_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_14_47_level.GetAssets().push_back(body_14_47_shape) 
body_14.GetAssets().push_back(body_14_47_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.082175575885392,0.208000000000001,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_14.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_14_49_shape = chrono.ChObjShapeFile() 
body_14_49_shape.SetFilename(shapes_dir +'body_14_49.obj') 
body_14_49_level = chrono.ChAssetLevel() 
body_14_49_level.GetFrame().SetPos(chrono.ChVectorD(0,0.1811,0.026)) 
body_14_49_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_14_49_level.GetAssets().push_back(body_14_49_shape) 
body_14.GetAssets().push_back(body_14_49_level) 

# Visualization shape 
body_14_50_shape = chrono.ChObjShapeFile() 
body_14_50_shape.SetFilename(shapes_dir +'body_14_50.obj') 
body_14_50_shape.SetColor(chrono.ChColor(0.101960784313725,0.101960784313725,0.101960784313725)) 
body_14_50_shape.SetFading(0) 
body_14_50_level = chrono.ChAssetLevel() 
body_14_50_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_14_50_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_14_50_level.GetAssets().push_back(body_14_50_shape) 
body_14.GetAssets().push_back(body_14_50_level) 

# Visualization shape 
body_6_36_shape = chrono.ChObjShapeFile() 
body_6_36_shape.SetFilename(shapes_dir +'body_6_36.obj') 
body_6_36_level = chrono.ChAssetLevel() 
body_6_36_level.GetFrame().SetPos(chrono.ChVectorD(0.085188180946079,0.139000000000001,0.05665)) 
body_6_36_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_36_level.GetAssets().push_back(body_6_36_shape) 
body_14.GetAssets().push_back(body_6_36_level) 

# Visualization shape 
body_7_44_shape = chrono.ChObjShapeFile() 
body_7_44_shape.SetFilename(shapes_dir +'body_7_44.obj') 
body_7_44_level = chrono.ChAssetLevel() 
body_7_44_level.GetFrame().SetPos(chrono.ChVectorD(0,0.1851,0.026)) 
body_7_44_level.GetFrame().SetRot(chrono.ChQuaternionD(6E-15,-5.61946013591574E-32,0,1)) 
body_7_44_level.GetAssets().push_back(body_7_44_shape) 
body_14.GetAssets().push_back(body_7_44_level) 

exported_items.append(body_14)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Torso.step-1/Torso.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_14 , SW name: Head.step-1/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0832334892503636,0.0964824589092795,0.425952088685129)
dA = chrono.ChVectorD(-5.2204844418111e-16,-3.49148133884314e-15,-1)
cB = chrono.ChVectorD(0.0832334892503633,0.0964824589092797,0.428852088685129)
dB = chrono.ChVectorD(1.24177384165393e-19,3.50286719851252e-15,1)
link_1.SetFlipped(True)
link_1.Initialize(body_9,body_14,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0832334892503636,0.0964824589092795,0.425952088685129)
cB = chrono.ChVectorD(0.0832334892503633,0.0964824589092797,0.428852088685129)
dA = chrono.ChVectorD(-5.2204844418111e-16,-3.49148133884314e-15,-1)
dB = chrono.ChVectorD(1.24177384165393e-19,3.50286719851252e-15,1)
link_2.Initialize(body_9,body_14,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Torso.step-1/Body.step-1/Base.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Head.step-1/Head.step-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00876651074963621,0.0704824589092789,0.428052088685129)
cB = chrono.ChVectorD(0.175233489250364,0.0703324589092873,0.430052088685129)
dA = chrono.ChVectorD(9.65411325760762e-17,3.49148133884313e-15,1)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_3.Initialize(body_9,body_14,False,cA,cB,dB)
link_3.SetDistance(-0.002)
link_3.SetName("Distance1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00876651074963621,0.0704824589092789,0.428052088685129)
dA = chrono.ChVectorD(9.65411325760762e-17,3.49148133884313e-15,1)
cB = chrono.ChVectorD(0.175233489250364,0.0703324589092873,0.430052088685129)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_4.SetFlipped(True)
link_4.Initialize(body_9,body_14,False,cA,cB,dA,dB)
link_4.SetName("Distance1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: Head.step-1/Head.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_12 , SW name: LH Shoulder.step-1/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.149139752618109,0.0855378597371208,0.441452088685129)
dA = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
cB = chrono.ChVectorD(0.149139752618109,0.0855378597371206,0.445352088685129)
dB = chrono.ChVectorD(9.65411325760769e-17,3.38098985565433e-15,1)
link_5.SetFlipped(True)
link_5.Initialize(body_14,body_12,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.149139752618109,0.0855378597371208,0.441452088685129)
cB = chrono.ChVectorD(0.149139752618109,0.0855378597371206,0.445352088685129)
dA = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
dB = chrono.ChVectorD(9.65411325760769e-17,3.38098985565433e-15,1)
link_6.Initialize(body_14,body_12,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_12 , SW name: LH Shoulder.step-1/Shoulder.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Head.step-1/Head.step-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.16423234716037,0.0956878597371388,0.496552088685129)
cB = chrono.ChVectorD(0.128341489250364,0.0703324589092872,0.499552088685129)
dA = chrono.ChVectorD(9.65411325760769e-17,3.38098985565433e-15,1)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_7.Initialize(body_12,body_14,False,cA,cB,dB)
link_7.SetDistance(-0.003)
link_7.SetName("Distance2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.16423234716037,0.0956878597371388,0.496552088685129)
dA = chrono.ChVectorD(9.65411325760769e-17,3.38098985565433e-15,1)
cB = chrono.ChVectorD(0.128341489250364,0.0703324589092872,0.499552088685129)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_8.SetFlipped(True)
link_8.Initialize(body_12,body_14,False,cA,cB,dA,dB)
link_8.SetName("Distance2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_12 , SW name: LH Shoulder.step-1/SG-5010 Cross Horn.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_6 , SW name: Upper Leg.step-1/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.192324941702632,0.0867378597372725,0.47855208868513)
dA = chrono.ChVectorD(1,6.83134104839667e-15,-9.65411325761e-17)
cB = chrono.ChVectorD(0.189624941702632,0.0867378597372725,0.47855208868513)
dB = chrono.ChVectorD(1,6.83827994230056e-15,-9.65411325760994e-17)
link_9.Initialize(body_12,body_6,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.192324941702632,0.0867378597372725,0.47855208868513)
cB = chrono.ChVectorD(0.189624941702632,0.0867378597372725,0.47855208868513)
dA = chrono.ChVectorD(1,6.83134104839667e-15,-9.65411325761e-17)
dB = chrono.ChVectorD(1,6.83827994230056e-15,-9.65411325760994e-17)
link_10.Initialize(body_12,body_6,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Upper Leg.step-1/Upper Leg-30.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: LH Shoulder.step-1/Shoulder Flange.step-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.241424941702632,0.0996878597372726,0.495552088685123)
cB = chrono.ChVectorD(0.244424941702632,0.0999628597372719,0.482777088685129)
dA = chrono.ChVectorD(1,6.83827994230058e-15,-1.93181864326587e-15)
dB = chrono.ChVectorD(-1,-6.83134104839667e-15,9.65411325761e-17)
link_11.Initialize(body_6,body_12,False,cA,cB,dB)
link_11.SetDistance(-0.003)
link_11.SetName("Distance3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.241424941702632,0.0996878597372726,0.495552088685123)
dA = chrono.ChVectorD(1,6.83827994230058e-15,-1.93181864326587e-15)
cB = chrono.ChVectorD(0.244424941702632,0.0999628597372719,0.482777088685129)
dB = chrono.ChVectorD(-1,-6.83134104839667e-15,9.65411325761e-17)
link_12.SetFlipped(True)
link_12.Initialize(body_6,body_12,False,cA,cB,dA,dB)
link_12.SetName("Distance3")
exported_items.append(link_12)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: Upper Leg.step-1/SG-5010 Cross Horn - Single Short.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_13 , SW name: Lower Leg.step-1/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.195324941702632,0.0666878597372736,0.345552088685122)
dA = chrono.ChVectorD(1,6.83827994230056e-15,-9.65411325760994e-17)
cB = chrono.ChVectorD(0.191624941702632,0.0666878597372736,0.345552088685122)
dB = chrono.ChVectorD(1,6.56072418614428e-15,-9.6541132576104e-17)
link_13.Initialize(body_6,body_13,False,cA,cB,dA,dB)
link_13.SetName("Concentric4")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.195324941702632,0.0666878597372736,0.345552088685122)
cB = chrono.ChVectorD(0.191624941702632,0.0666878597372736,0.345552088685122)
dA = chrono.ChVectorD(1,6.83827994230056e-15,-9.65411325760994e-17)
dB = chrono.ChVectorD(1,6.56072418614428e-15,-9.6541132576104e-17)
link_14.Initialize(body_6,body_13,False,cA,cB,dA,dB)
link_14.SetName("Concentric4")
exported_items.append(link_14)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: Lower Leg.step-1/Lower Leg.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Upper Leg.step-1/Upper Leg-30.step-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.239424941702632,0.0652378597372732,0.412052088759635)
cB = chrono.ChVectorD(0.242424941702632,0.0666878597372742,0.346373156496987)
dA = chrono.ChVectorD(1,6.56072418614428e-15,-9.6541132576104e-17)
dB = chrono.ChVectorD(-1,-6.83827994230057e-15,1.0965411325761e-15)
link_15.Initialize(body_13,body_6,False,cA,cB,dB)
link_15.SetDistance(-0.003)
link_15.SetName("Distance4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.239424941702632,0.0652378597372732,0.412052088759635)
dA = chrono.ChVectorD(1,6.56072418614428e-15,-9.6541132576104e-17)
cB = chrono.ChVectorD(0.242424941702632,0.0666878597372742,0.346373156496987)
dB = chrono.ChVectorD(-1,-6.83827994230057e-15,1.0965411325761e-15)
link_16.SetFlipped(True)
link_16.Initialize(body_13,body_6,False,cA,cB,dA,dB)
link_16.SetName("Distance4")
exported_items.append(link_16)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Lower Leg.step-3/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: Upper Leg.step-3/SG-5010 Cross Horn - Single Short.step-1 ,  SW ref.type:1 (1)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.191624941702626,0.0668378597372513,0.110052088685122)
dA = chrono.ChVectorD(1,-3.34378358335385e-13,-2.15206590129525e-17)
cB = chrono.ChVectorD(0.195324941702625,0.0668378597372501,0.110052088685122)
dB = chrono.ChVectorD(1,-3.34603872387262e-13,-2.15206590129469e-17)
link_17.Initialize(body_8,body_10,False,cA,cB,dA,dB)
link_17.SetName("Concentric7")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.191624941702626,0.0668378597372513,0.110052088685122)
cB = chrono.ChVectorD(0.195324941702625,0.0668378597372501,0.110052088685122)
dA = chrono.ChVectorD(1,-3.34378358335385e-13,-2.15206590129525e-17)
dB = chrono.ChVectorD(1,-3.34603872387262e-13,-2.15206590129469e-17)
link_18.Initialize(body_8,body_10,False,cA,cB,dA,dB)
link_18.SetName("Concentric7")
exported_items.append(link_18)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Lower Leg.step-3/Lower Leg.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Upper Leg.step-3/Upper Leg-30.step-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.239424941702625,0.0653878597372347,0.176552088759634)
cB = chrono.ChVectorD(0.242424941702625,0.0668378597372346,0.110873156496987)
dA = chrono.ChVectorD(1,-3.34378358335385e-13,-2.15206590129525e-17)
dB = chrono.ChVectorD(-1,3.34603872387262e-13,1.02152065901295e-15)
link_19.Initialize(body_8,body_10,False,cA,cB,dB)
link_19.SetDistance(-0.003)
link_19.SetName("Distance7")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.239424941702625,0.0653878597372347,0.176552088759634)
dA = chrono.ChVectorD(1,-3.34378358335385e-13,-2.15206590129525e-17)
cB = chrono.ChVectorD(0.242424941702625,0.0668378597372346,0.110873156496987)
dB = chrono.ChVectorD(-1,3.34603872387262e-13,1.02152065901295e-15)
link_20.SetFlipped(True)
link_20.Initialize(body_8,body_10,False,cA,cB,dA,dB)
link_20.SetName("Distance7")
exported_items.append(link_20)


# Mate constraint: Concentric8 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Torso.step-1/Body.step-1/Base.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_7 , SW name: LH Shoulder.step-3/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.149139752618109,0.0856878597371129,0.199952088685129)
dA = chrono.ChVectorD(-4.03717463500033e-16,-3.49148133884314e-15,-1)
cB = chrono.ChVectorD(0.149139752618109,0.0856878597371129,0.209852088685129)
dB = chrono.ChVectorD(2.15206590140818e-17,3.39197697425342e-15,1)
link_21.SetFlipped(True)
link_21.Initialize(body_9,body_7,False,cA,cB,dA,dB)
link_21.SetName("Concentric8")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.149139752618109,0.0856878597371129,0.199952088685129)
cB = chrono.ChVectorD(0.149139752618109,0.0856878597371129,0.209852088685129)
dA = chrono.ChVectorD(-4.03717463500033e-16,-3.49148133884314e-15,-1)
dB = chrono.ChVectorD(2.15206590140818e-17,3.39197697425342e-15,1)
link_22.Initialize(body_9,body_7,False,cA,cB,dA,dB)
link_22.SetName("Concentric8")
exported_items.append(link_22)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_7 , SW name: LH Shoulder.step-3/Shoulder.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Torso.step-1/Body.step-1/Base.step-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.164232347160374,0.0958378597371259,0.261052088685129)
cB = chrono.ChVectorD(-0.00876651074963621,0.0704824589092783,0.258052088685129)
dA = chrono.ChVectorD(2.15206590140818e-17,3.39197697425342e-15,1)
dB = chrono.ChVectorD(-1.51527496323486e-15,-3.49148133884314e-15,-1)
link_23.Initialize(body_7,body_9,False,cA,cB,dB)
link_23.SetDistance(0.003)
link_23.SetName("Distance8")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.164232347160374,0.0958378597371259,0.261052088685129)
dA = chrono.ChVectorD(2.15206590140818e-17,3.39197697425342e-15,1)
cB = chrono.ChVectorD(-0.00876651074963621,0.0704824589092783,0.258052088685129)
dB = chrono.ChVectorD(-1.51527496323486e-15,-3.49148133884314e-15,-1)
link_24.SetFlipped(True)
link_24.Initialize(body_7,body_9,False,cA,cB,dA,dB)
link_24.SetName("Distance8")
exported_items.append(link_24)


# Mate constraint: Concentric9 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: LH Shoulder.step-3/SG-5010 Cross Horn.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: Upper Leg.step-3/Sunfounder Servo 55g.step-1/Sunfounder Servo 55g-1.step-1 ,  SW ref.type:1 (1)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.192324941702632,0.08688785973725,0.243052088685129)
dA = chrono.ChVectorD(1,-3.34593464046407e-13,-2.1520659012947e-17)
cB = chrono.ChVectorD(0.189624941702632,0.0868878597372509,0.243052088685129)
dB = chrono.ChVectorD(1,-3.34603872387262e-13,-2.15206590129469e-17)
link_25.Initialize(body_7,body_10,False,cA,cB,dA,dB)
link_25.SetName("Concentric9")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.192324941702632,0.08688785973725,0.243052088685129)
cB = chrono.ChVectorD(0.189624941702632,0.0868878597372509,0.243052088685129)
dA = chrono.ChVectorD(1,-3.34593464046407e-13,-2.1520659012947e-17)
dB = chrono.ChVectorD(1,-3.34603872387262e-13,-2.15206590129469e-17)
link_26.Initialize(body_7,body_10,False,cA,cB,dA,dB)
link_26.SetName("Concentric9")
exported_items.append(link_26)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_10 , SW name: Upper Leg.step-3/Upper Leg-30.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: LH Shoulder.step-3/Shoulder Flange.step-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.241424941702637,0.0998378597372334,0.260052088685122)
cB = chrono.ChVectorD(0.244424941702636,0.100112859737232,0.247277088685129)
dA = chrono.ChVectorD(1,-3.34603872387262e-13,-1.85679816970272e-15)
dB = chrono.ChVectorD(-1,3.34593464046407e-13,2.1520659012947e-17)
link_27.Initialize(body_10,body_7,False,cA,cB,dB)
link_27.SetDistance(-0.003)
link_27.SetName("Distance9")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.241424941702637,0.0998378597372334,0.260052088685122)
dA = chrono.ChVectorD(1,-3.34603872387262e-13,-1.85679816970272e-15)
cB = chrono.ChVectorD(0.244424941702636,0.100112859737232,0.247277088685129)
dB = chrono.ChVectorD(-1,3.34593464046407e-13,2.1520659012947e-17)
link_28.SetFlipped(True)
link_28.Initialize(body_10,body_7,False,cA,cB,dA,dB)
link_28.SetName("Distance9")
exported_items.append(link_28)


# Mate constraint: Concentric10 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: RH Upper Leg.step-1/SG-5010 Cross Horn - Single Short v2(Mirror).step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_4 , SW name: RH Lower Leg.step-1/Sunfounder Servo 55g v8(Mirror) (2).step-1/Sunfounder Servo 55g v8(Mirror) (2)-1.step-1 ,  SW ref.type:1 (1)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.028857963201902,0.0666878597372655,0.345552088685123)
dA = chrono.ChVectorD(1,-3.49148133884313e-30,-7.98296267768627e-15)
cB = chrono.ChVectorD(-0.0251579632019024,0.0666878597372661,0.345552088685123)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_29.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_29.SetName("Concentric10")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.028857963201902,0.0666878597372655,0.345552088685123)
cB = chrono.ChVectorD(-0.0251579632019024,0.0666878597372661,0.345552088685123)
dA = chrono.ChVectorD(1,-3.49148133884313e-30,-7.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_30.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_30.SetName("Concentric10")
exported_items.append(link_30)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: RH Lower Leg.step-1/Lower Leg(Mirror).step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: RH Upper Leg.step-1/Upper Leg(Mirror)-30.step-1 ,  SW ref.type:2 (2)

link_31 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0729579632019019,0.0652378597372663,0.412052088759636)
cB = chrono.ChVectorD(-0.0759579632019021,0.0666878597372658,0.346373156496989)
dA = chrono.ChVectorD(-1,0,6.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_31.Initialize(body_4,body_1,False,cA,cB,dB)
link_31.SetDistance(-0.003)
link_31.SetName("Distance10")
exported_items.append(link_31)

link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0729579632019019,0.0652378597372663,0.412052088759636)
dA = chrono.ChVectorD(-1,0,6.98296267768627e-15)
cB = chrono.ChVectorD(-0.0759579632019021,0.0666878597372658,0.346373156496989)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_32.SetFlipped(True)
link_32.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_32.SetName("Distance10")
exported_items.append(link_32)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_11 , SW name: RH Shoulder.step-1/SG-5010 Cross Horn v3(Mirror).step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_1 , SW name: RH Upper Leg.step-1/Sunfounder Servo 55g v8(Mirror) (1).step-1/Sunfounder Servo 55g v8(Mirror) (1)-1.step-1 ,  SW ref.type:1 (1)

link_33 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.025857963201901,0.0867378597372715,0.47855208868513)
dA = chrono.ChVectorD(1,0,-6.98296267768627e-15)
cB = chrono.ChVectorD(-0.0231579632019011,0.0867378597372662,0.478552088685131)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_33.Initialize(body_11,body_1,False,cA,cB,dA,dB)
link_33.SetName("Concentric11")
exported_items.append(link_33)

link_34 = chrono.ChLinkMateGeneric()
link_34.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.025857963201901,0.0867378597372715,0.47855208868513)
cB = chrono.ChVectorD(-0.0231579632019011,0.0867378597372662,0.478552088685131)
dA = chrono.ChVectorD(1,0,-6.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_34.Initialize(body_11,body_1,False,cA,cB,dA,dB)
link_34.SetName("Concentric11")
exported_items.append(link_34)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: RH Upper Leg.step-1/Upper Leg(Mirror)-30.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: RH Shoulder.step-1/Shoulder Flange(Mirror).step-1 ,  SW ref.type:2 (2)

link_35 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.074957963201901,0.0996878597372663,0.495552088685124)
cB = chrono.ChVectorD(-0.077957963201901,0.0999628597372706,0.48277708868513)
dA = chrono.ChVectorD(-1,-2.947267318806e-30,6.14768516699649e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_35.Initialize(body_1,body_11,False,cA,cB,dB)
link_35.SetDistance(-0.003)
link_35.SetName("Distance11")
exported_items.append(link_35)

link_36 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.074957963201901,0.0996878597372663,0.495552088685124)
dA = chrono.ChVectorD(-1,-2.947267318806e-30,6.14768516699649e-15)
cB = chrono.ChVectorD(-0.077957963201901,0.0999628597372706,0.48277708868513)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_36.SetFlipped(True)
link_36.Initialize(body_1,body_11,False,cA,cB,dA,dB)
link_36.SetName("Distance11")
exported_items.append(link_36)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: Head.step-1/Head.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_11 , SW name: RH Shoulder.step-1/Sunfounder Servo 55g v8(Mirror).step-1/Sunfounder Servo 55g v8(Mirror)-1.step-1 ,  SW ref.type:1 (1)

link_37 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0173272258826182,0.0855378597371199,0.441452088685129)
dA = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
cB = chrono.ChVectorD(0.0173272258826215,0.08553785973712,0.445352088685129)
dB = chrono.ChVectorD(-6.98296267768627e-15,-3.49148133884313e-15,-1)
link_37.Initialize(body_14,body_11,False,cA,cB,dA,dB)
link_37.SetName("Concentric12")
exported_items.append(link_37)

link_38 = chrono.ChLinkMateGeneric()
link_38.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0173272258826182,0.0855378597371199,0.441452088685129)
cB = chrono.ChVectorD(0.0173272258826215,0.08553785973712,0.445352088685129)
dA = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
dB = chrono.ChVectorD(-6.98296267768627e-15,-3.49148133884313e-15,-1)
link_38.Initialize(body_14,body_11,False,cA,cB,dA,dB)
link_38.SetName("Concentric12")
exported_items.append(link_38)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: RH Shoulder.step-1/Shoulder(Mirror).step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Head.step-1/Head.step-1 ,  SW ref.type:2 (2)

link_39 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00223463134036057,0.095687859737138,0.496552088685129)
cB = chrono.ChVectorD(-0.00876651074963648,0.0703324589092862,0.499552088685129)
dA = chrono.ChVectorD(6.98296267768627e-15,3.49148133884313e-15,1)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_39.Initialize(body_11,body_14,False,cA,cB,dB)
link_39.SetDistance(-0.003)
link_39.SetName("Distance12")
exported_items.append(link_39)

link_40 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00223463134036057,0.095687859737138,0.496552088685129)
dA = chrono.ChVectorD(6.98296267768627e-15,3.49148133884313e-15,1)
cB = chrono.ChVectorD(-0.00876651074963648,0.0703324589092862,0.499552088685129)
dB = chrono.ChVectorD(-1.24177384165393e-19,-3.50286719851252e-15,-1)
link_40.SetFlipped(True)
link_40.Initialize(body_11,body_14,False,cA,cB,dA,dB)
link_40.SetName("Distance12")
exported_items.append(link_40)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: RH Upper Leg.step-2/Sunfounder Servo 55g v8(Mirror) (1).step-1/Sunfounder Servo 55g v8(Mirror) (1)-1.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_5 , SW name: RH Shoulder.step-2/SG-5010 Cross Horn v3(Mirror).step-1 ,  SW ref.type:1 (1)

link_41 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0231579632018997,0.0868878597372612,0.237052088685131)
dA = chrono.ChVectorD(1,0,-6.98296267768627e-15)
cB = chrono.ChVectorD(-0.0258579632018996,0.0868878597372636,0.23705208868513)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_41.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_41.SetName("Concentric13")
exported_items.append(link_41)

link_42 = chrono.ChLinkMateGeneric()
link_42.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0231579632018997,0.0868878597372612,0.237052088685131)
cB = chrono.ChVectorD(-0.0258579632018996,0.0868878597372636,0.23705208868513)
dA = chrono.ChVectorD(1,0,-6.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_42.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_42.SetName("Concentric13")
exported_items.append(link_42)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: RH Lower Leg.step-2/Lower Leg(Mirror).step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: RH Upper Leg.step-2/Upper Leg(Mirror)-30.step-1 ,  SW ref.type:2 (2)

link_43 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0729579632019003,0.0653878597372608,0.170552088759636)
cB = chrono.ChVectorD(-0.0759579632019006,0.0668378597372607,0.104873156496989)
dA = chrono.ChVectorD(-1,0,6.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_43.Initialize(body_3,body_2,False,cA,cB,dB)
link_43.SetDistance(-0.003)
link_43.SetName("Distance13")
exported_items.append(link_43)

link_44 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0729579632019003,0.0653878597372608,0.170552088759636)
dA = chrono.ChVectorD(-1,0,6.98296267768627e-15)
cB = chrono.ChVectorD(-0.0759579632019006,0.0668378597372607,0.104873156496989)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_44.SetFlipped(True)
link_44.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_44.SetName("Distance13")
exported_items.append(link_44)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: RH Upper Leg.step-2/Upper Leg(Mirror)-30.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: RH Shoulder.step-2/Shoulder Flange(Mirror).step-1 ,  SW ref.type:2 (2)

link_45 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0749579632018996,0.0998378597372612,0.254052088685124)
cB = chrono.ChVectorD(-0.0779579632018996,0.100112859737263,0.24127708868513)
dA = chrono.ChVectorD(-1,-2.947267318806e-30,6.14768516699649e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_45.Initialize(body_2,body_5,False,cA,cB,dB)
link_45.SetDistance(-0.003)
link_45.SetName("Distance14")
exported_items.append(link_45)

link_46 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0749579632018996,0.0998378597372612,0.254052088685124)
dA = chrono.ChVectorD(-1,-2.947267318806e-30,6.14768516699649e-15)
cB = chrono.ChVectorD(-0.0779579632018996,0.100112859737263,0.24127708868513)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_46.SetFlipped(True)
link_46.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_46.SetName("Distance14")
exported_items.append(link_46)


# Mate constraint: Concentric14 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: RH Upper Leg.step-2/SG-5010 Cross Horn - Single Short v2(Mirror).step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_3 , SW name: RH Lower Leg.step-2/Sunfounder Servo 55g v8(Mirror) (2).step-1/Sunfounder Servo 55g v8(Mirror) (2)-1.step-1 ,  SW ref.type:1 (1)

link_47 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0288579632019006,0.0668378597372604,0.104052088685123)
dA = chrono.ChVectorD(1,-3.49148133884313e-30,-7.98296267768627e-15)
cB = chrono.ChVectorD(-0.0251579632019007,0.0668378597372606,0.104052088685123)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_47.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_47.SetName("Concentric14")
exported_items.append(link_47)

link_48 = chrono.ChLinkMateGeneric()
link_48.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0288579632019006,0.0668378597372604,0.104052088685123)
cB = chrono.ChVectorD(-0.0251579632019007,0.0668378597372606,0.104052088685123)
dA = chrono.ChVectorD(1,-3.49148133884313e-30,-7.98296267768627e-15)
dB = chrono.ChVectorD(1,0,-6.98296267768627e-15)
link_48.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_48.SetName("Concentric14")
exported_items.append(link_48)


# Mate constraint: Concentric15 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Torso.step-1/Body.step-1/Base.step-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_5 , SW name: RH Shoulder.step-2/Sunfounder Servo 55g v8(Mirror).step-1/Sunfounder Servo 55g v8(Mirror)-1.step-1 ,  SW ref.type:1 (1)

link_49 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0173272258826185,0.0856878597371119,0.199952088685129)
dA = chrono.ChVectorD(-4.03717463500033e-16,-3.49148133884314e-15,-1)
cB = chrono.ChVectorD(0.017327225882623,0.085687859737112,0.203852088685129)
dB = chrono.ChVectorD(-6.98296267768627e-15,-3.49148133884313e-15,-1)
link_49.Initialize(body_9,body_5,False,cA,cB,dA,dB)
link_49.SetName("Concentric15")
exported_items.append(link_49)

link_50 = chrono.ChLinkMateGeneric()
link_50.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0173272258826185,0.0856878597371119,0.199952088685129)
cB = chrono.ChVectorD(0.017327225882623,0.085687859737112,0.203852088685129)
dA = chrono.ChVectorD(-4.03717463500033e-16,-3.49148133884314e-15,-1)
dB = chrono.ChVectorD(-6.98296267768627e-15,-3.49148133884313e-15,-1)
link_50.Initialize(body_9,body_5,False,cA,cB,dA,dB)
link_50.SetName("Concentric15")
exported_items.append(link_50)


# Mate constraint: Distance15 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: RH Shoulder.step-2/Shoulder(Mirror).step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Torso.step-1/Body.step-1/Base.step-1 ,  SW ref.type:2 (2)

link_51 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00223463134036202,0.0958378597371301,0.255052088685129)
cB = chrono.ChVectorD(-0.00876651074963621,0.0704824589092783,0.258052088685129)
dA = chrono.ChVectorD(6.98296267768627e-15,3.49148133884313e-15,1)
dB = chrono.ChVectorD(-1.51527496323486e-15,-3.49148133884314e-15,-1)
link_51.Initialize(body_5,body_9,False,cA,cB,dB)
link_51.SetDistance(-0.003)
link_51.SetName("Distance15")
exported_items.append(link_51)

link_52 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00223463134036202,0.0958378597371301,0.255052088685129)
dA = chrono.ChVectorD(6.98296267768627e-15,3.49148133884313e-15,1)
cB = chrono.ChVectorD(-0.00876651074963621,0.0704824589092783,0.258052088685129)
dB = chrono.ChVectorD(-1.51527496323486e-15,-3.49148133884314e-15,-1)
link_52.SetFlipped(True)
link_52.Initialize(body_5,body_9,False,cA,cB,dA,dB)
link_52.SetName("Distance15")
exported_items.append(link_52)

