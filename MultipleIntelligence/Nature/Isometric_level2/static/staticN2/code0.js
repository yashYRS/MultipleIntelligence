gdjs.Rules2Code = {};
gdjs.Rules2Code.GDRule2Objects1= [];
gdjs.Rules2Code.GDRule2Objects2= [];
gdjs.Rules2Code.GDRuleObjects1= [];
gdjs.Rules2Code.GDRuleObjects2= [];
gdjs.Rules2Code.GDmanObjects1= [];
gdjs.Rules2Code.GDmanObjects2= [];
gdjs.Rules2Code.GDRule3Objects1= [];
gdjs.Rules2Code.GDRule3Objects2= [];

gdjs.Rules2Code.conditionTrue_0 = {val:false};
gdjs.Rules2Code.condition0IsTrue_0 = {val:false};
gdjs.Rules2Code.condition1IsTrue_0 = {val:false};


gdjs.Rules2Code.mapOfGDgdjs_46Rules2Code_46GDRule3Objects1Objects = Hashtable.newFrom({"Rule3": gdjs.Rules2Code.GDRule3Objects1});gdjs.Rules2Code.eventsList0x71f4c8 = function(runtimeScene) {

{


gdjs.Rules2Code.condition0IsTrue_0.val = false;
{
gdjs.Rules2Code.condition0IsTrue_0.val = gdjs.evtTools.input.isMouseButtonReleased(runtimeScene, "Left");
}if (gdjs.Rules2Code.condition0IsTrue_0.val) {
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Level2", false);
}}

}


}; //End of gdjs.Rules2Code.eventsList0x71f4c8
gdjs.Rules2Code.eventsList0xb0cf8 = function(runtimeScene) {

{

gdjs.Rules2Code.GDRule3Objects1.createFrom(runtimeScene.getObjects("Rule3"));

gdjs.Rules2Code.condition0IsTrue_0.val = false;
{
gdjs.Rules2Code.condition0IsTrue_0.val = gdjs.evtTools.input.cursorOnObject(gdjs.Rules2Code.mapOfGDgdjs_46Rules2Code_46GDRule3Objects1Objects, runtimeScene, true, false);
}if (gdjs.Rules2Code.condition0IsTrue_0.val) {

{ //Subevents
gdjs.Rules2Code.eventsList0x71f4c8(runtimeScene);} //End of subevents
}

}


}; //End of gdjs.Rules2Code.eventsList0xb0cf8


gdjs.Rules2Code.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();
gdjs.Rules2Code.GDRule2Objects1.length = 0;
gdjs.Rules2Code.GDRule2Objects2.length = 0;
gdjs.Rules2Code.GDRuleObjects1.length = 0;
gdjs.Rules2Code.GDRuleObjects2.length = 0;
gdjs.Rules2Code.GDmanObjects1.length = 0;
gdjs.Rules2Code.GDmanObjects2.length = 0;
gdjs.Rules2Code.GDRule3Objects1.length = 0;
gdjs.Rules2Code.GDRule3Objects2.length = 0;

gdjs.Rules2Code.eventsList0xb0cf8(runtimeScene);
return;
}
gdjs['Rules2Code'] = gdjs.Rules2Code;
