gdjs.Rules1Code = {};
gdjs.Rules1Code.GDRule2Objects1= [];
gdjs.Rules1Code.GDRule2Objects2= [];
gdjs.Rules1Code.GDRuleObjects1= [];
gdjs.Rules1Code.GDRuleObjects2= [];
gdjs.Rules1Code.GDmindaObjects1= [];
gdjs.Rules1Code.GDmindaObjects2= [];
gdjs.Rules1Code.GDRule3Objects1= [];
gdjs.Rules1Code.GDRule3Objects2= [];

gdjs.Rules1Code.conditionTrue_0 = {val:false};
gdjs.Rules1Code.condition0IsTrue_0 = {val:false};
gdjs.Rules1Code.condition1IsTrue_0 = {val:false};


gdjs.Rules1Code.mapOfGDgdjs_46Rules1Code_46GDRule3Objects1Objects = Hashtable.newFrom({"Rule3": gdjs.Rules1Code.GDRule3Objects1});gdjs.Rules1Code.eventsList0x8a0e70 = function(runtimeScene) {

{


gdjs.Rules1Code.condition0IsTrue_0.val = false;
{
gdjs.Rules1Code.condition0IsTrue_0.val = gdjs.evtTools.input.isMouseButtonReleased(runtimeScene, "Left");
}if (gdjs.Rules1Code.condition0IsTrue_0.val) {
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Level1", false);
}}

}


}; //End of gdjs.Rules1Code.eventsList0x8a0e70
gdjs.Rules1Code.eventsList0xb0cf8 = function(runtimeScene) {

{

gdjs.Rules1Code.GDRule3Objects1.createFrom(runtimeScene.getObjects("Rule3"));

gdjs.Rules1Code.condition0IsTrue_0.val = false;
{
gdjs.Rules1Code.condition0IsTrue_0.val = gdjs.evtTools.input.cursorOnObject(gdjs.Rules1Code.mapOfGDgdjs_46Rules1Code_46GDRule3Objects1Objects, runtimeScene, true, false);
}if (gdjs.Rules1Code.condition0IsTrue_0.val) {

{ //Subevents
gdjs.Rules1Code.eventsList0x8a0e70(runtimeScene);} //End of subevents
}

}


}; //End of gdjs.Rules1Code.eventsList0xb0cf8


gdjs.Rules1Code.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();
gdjs.Rules1Code.GDRule2Objects1.length = 0;
gdjs.Rules1Code.GDRule2Objects2.length = 0;
gdjs.Rules1Code.GDRuleObjects1.length = 0;
gdjs.Rules1Code.GDRuleObjects2.length = 0;
gdjs.Rules1Code.GDmindaObjects1.length = 0;
gdjs.Rules1Code.GDmindaObjects2.length = 0;
gdjs.Rules1Code.GDRule3Objects1.length = 0;
gdjs.Rules1Code.GDRule3Objects2.length = 0;

gdjs.Rules1Code.eventsList0xb0cf8(runtimeScene);
return;
}
gdjs['Rules1Code'] = gdjs.Rules1Code;
