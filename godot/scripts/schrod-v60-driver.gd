tool
extends Spatial


# Declare member variables here. Examples:
export var fr := Vector3(0, 0, 0)
export var fl := Vector3(0, 0, 0)
export var br := Vector3(0, 0, 0)
export var bl := Vector3(0, 0, 0)
export var neck := 0.0

onready var fr_joints = [
	$"torso/head/shoulder-fr",
	$"torso/head/shoulder-fr/thigh",
	$"torso/head/shoulder-fr/thigh/shin"
]
onready var fl_joints = [
	$"torso/head/shoulder-fl",
	$"torso/head/shoulder-fl/thigh",
	$"torso/head/shoulder-fl/thigh/shin"
]
onready var br_joints = [
	$"torso/shoulder-br",
	$"torso/shoulder-br/thigh",
	$"torso/shoulder-br/thigh/shin"
]
onready var bl_joints = [
	$"torso/shoulder-bl",
	$"torso/shoulder-bl/thigh",
	$"torso/shoulder-bl/thigh/shin"
]
onready var neck_joint = $"torso/head"


# Called when the node enters the scene tree for the first time.
func _ready():
	neck_joint.rotation
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Joints on the right have one set of constant offsets
	fr_joints[0].rotation = Vector3(PI, 0, -fr[0])
	fr_joints[1].rotation = Vector3(fr[1], 0, 0)
	fr_joints[2].rotation = Vector3(-fr[2], 0, 0)
	
	br_joints[0].rotation = Vector3(PI, 0, -br[0])
	br_joints[1].rotation = Vector3(br[1], 0, 0)
	br_joints[2].rotation = Vector3(-br[2], 0, 0)
	
	# Joints on the left have another set of constant offsets
	fl_joints[0].rotation = Vector3(0, PI, -fl[0])
	fl_joints[1].rotation = Vector3(-fl[1], 0, 0)
	fl_joints[2].rotation = Vector3(fl[2], 0, 0)
	
	bl_joints[0].rotation = Vector3(0, PI, -bl[0])
	bl_joints[1].rotation = Vector3(-bl[1], 0, 0)
	bl_joints[2].rotation = Vector3(bl[2], 0, 0)
	
	neck_joint.rotation = Vector3(0, 0, neck)
