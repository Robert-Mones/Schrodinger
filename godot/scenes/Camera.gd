tool
extends Camera


# Declare member variables here. Examples:
export var target : NodePath
export var offset : Vector3  = Vector3(0, 0, -2)

var targetNode : Spatial = null

# Called when the node enters the scene tree for the first time.
func _ready():
	targetNode = get_node(target) as Spatial

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if (targetNode == null):
		return
	
	var targetPos = targetNode.get_parent_spatial().to_global(targetNode.translation)
	translation = targetPos + offset;
	look_at(targetPos, Vector3(0,1,0))
