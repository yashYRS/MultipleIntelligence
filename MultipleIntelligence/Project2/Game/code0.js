gdjs.Scene1Code = {};
gdjs.Scene1Code.GDHeroObjects1= [];
gdjs.Scene1Code.GDHeroObjects2= [];
gdjs.Scene1Code.GDRedDoorObjects1= [];
gdjs.Scene1Code.GDRedDoorObjects2= [];
gdjs.Scene1Code.GDRedDoor2Objects1= [];
gdjs.Scene1Code.GDRedDoor2Objects2= [];
gdjs.Scene1Code.GDRedDoor3Objects1= [];
gdjs.Scene1Code.GDRedDoor3Objects2= [];
gdjs.Scene1Code.GDUpObjects1= [];
gdjs.Scene1Code.GDUpObjects2= [];
gdjs.Scene1Code.GDDownObjects1= [];
gdjs.Scene1Code.GDDownObjects2= [];
gdjs.Scene1Code.GDTextObjects1= [];
gdjs.Scene1Code.GDTextObjects2= [];
gdjs.Scene1Code.GDBoxObjects1= [];
gdjs.Scene1Code.GDBoxObjects2= [];

gdjs.Scene1Code.conditionTrue_0 = {val:false};
gdjs.Scene1Code.condition0IsTrue_0 = {val:false};
gdjs.Scene1Code.condition1IsTrue_0 = {val:false};
gdjs.Scene1Code.condition2IsTrue_0 = {val:false};


gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDHeroObjects1Objects = Hashtable.newFrom({"Hero": gdjs.Scene1Code.GDHeroObjects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDUpObjects1Objects = Hashtable.newFrom({"Up": gdjs.Scene1Code.GDUpObjects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDHeroObjects1Objects = Hashtable.newFrom({"Hero": gdjs.Scene1Code.GDHeroObjects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDDownObjects1Objects = Hashtable.newFrom({"Down": gdjs.Scene1Code.GDDownObjects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoorObjects1Objects = Hashtable.newFrom({"RedDoor": gdjs.Scene1Code.GDRedDoorObjects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoor2Objects1Objects = Hashtable.newFrom({"RedDoor2": gdjs.Scene1Code.GDRedDoor2Objects1});gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoor3Objects1Objects = Hashtable.newFrom({"RedDoor3": gdjs.Scene1Code.GDRedDoor3Objects1});gdjs.Scene1Code.eventsList0xb0cf8 = function(runtimeScene) {

{


gdjs.Scene1Code.condition0IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.runtimeScene.sceneJustBegins(runtimeScene);
}if (gdjs.Scene1Code.condition0IsTrue_0.val) {
gdjs.Scene1Code.GDDownObjects1.createFrom(runtimeScene.getObjects("Down"));
gdjs.Scene1Code.GDUpObjects1.createFrom(runtimeScene.getObjects("Up"));
{for(var i = 0, len = gdjs.Scene1Code.GDUpObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDUpObjects1[i].hide();
}
}{for(var i = 0, len = gdjs.Scene1Code.GDDownObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDDownObjects1[i].hide();
}
}}

}


{

gdjs.Scene1Code.GDHeroObjects1.createFrom(runtimeScene.getObjects("Hero"));
gdjs.Scene1Code.GDUpObjects1.createFrom(runtimeScene.getObjects("Up"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.object.hitBoxesCollisionTest(gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDHeroObjects1Objects, gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDUpObjects1Objects, false, runtimeScene, false);
}if (gdjs.Scene1Code.condition0IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDHeroObjects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDHeroObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDHeroObjects1[i].returnVariable(gdjs.Scene1Code.GDHeroObjects1[i].getVariables().getFromIndex(0)).setString("Up");
}
}}

}


{

gdjs.Scene1Code.GDDownObjects1.createFrom(runtimeScene.getObjects("Down"));
gdjs.Scene1Code.GDHeroObjects1.createFrom(runtimeScene.getObjects("Hero"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.object.hitBoxesCollisionTest(gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDHeroObjects1Objects, gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDDownObjects1Objects, false, runtimeScene, false);
}if (gdjs.Scene1Code.condition0IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDHeroObjects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDHeroObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDHeroObjects1[i].returnVariable(gdjs.Scene1Code.GDHeroObjects1[i].getVariables().getFromIndex(0)).setString("Down");
}
}}

}


{

gdjs.Scene1Code.GDHeroObjects1.createFrom(runtimeScene.getObjects("Hero"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
{
for(var i = 0, k = 0, l = gdjs.Scene1Code.GDHeroObjects1.length;i<l;++i) {
    if ( gdjs.Scene1Code.GDHeroObjects1[i].getVariableString(gdjs.Scene1Code.GDHeroObjects1[i].getVariables().getFromIndex(0)) == "Down" ) {
        gdjs.Scene1Code.condition0IsTrue_0.val = true;
        gdjs.Scene1Code.GDHeroObjects1[k] = gdjs.Scene1Code.GDHeroObjects1[i];
        ++k;
    }
}
gdjs.Scene1Code.GDHeroObjects1.length = k;}if (gdjs.Scene1Code.condition0IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDHeroObjects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDHeroObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDHeroObjects1[i].addPolarForce(90, 25, 0);
}
}}

}


{

gdjs.Scene1Code.GDHeroObjects1.createFrom(runtimeScene.getObjects("Hero"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
{
for(var i = 0, k = 0, l = gdjs.Scene1Code.GDHeroObjects1.length;i<l;++i) {
    if ( gdjs.Scene1Code.GDHeroObjects1[i].getVariableString(gdjs.Scene1Code.GDHeroObjects1[i].getVariables().getFromIndex(0)) == "Up" ) {
        gdjs.Scene1Code.condition0IsTrue_0.val = true;
        gdjs.Scene1Code.GDHeroObjects1[k] = gdjs.Scene1Code.GDHeroObjects1[i];
        ++k;
    }
}
gdjs.Scene1Code.GDHeroObjects1.length = k;}if (gdjs.Scene1Code.condition0IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDHeroObjects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDHeroObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDHeroObjects1[i].addPolarForce(270, 25, 0);
}
}}

}


{

gdjs.Scene1Code.GDRedDoorObjects1.createFrom(runtimeScene.getObjects("RedDoor"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
gdjs.Scene1Code.condition1IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.input.isMouseButtonPressed(runtimeScene, "Left");
}if ( gdjs.Scene1Code.condition0IsTrue_0.val ) {
{
gdjs.Scene1Code.condition1IsTrue_0.val = gdjs.evtTools.input.cursorOnObject(gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoorObjects1Objects, runtimeScene, true, false);
}}
if (gdjs.Scene1Code.condition1IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDRedDoorObjects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDRedDoorObjects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDRedDoorObjects1[i].setAnimationName("Open");
}
}{gdjs.evtTools.sound.playSound(runtimeScene, "Audio\\door-1-open.wav", false, 100, 1);
}{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Scene2", false);
}}

}


{

gdjs.Scene1Code.GDRedDoor2Objects1.createFrom(runtimeScene.getObjects("RedDoor2"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
gdjs.Scene1Code.condition1IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.input.isMouseButtonPressed(runtimeScene, "Left");
}if ( gdjs.Scene1Code.condition0IsTrue_0.val ) {
{
gdjs.Scene1Code.condition1IsTrue_0.val = gdjs.evtTools.input.cursorOnObject(gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoor2Objects1Objects, runtimeScene, true, false);
}}
if (gdjs.Scene1Code.condition1IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDRedDoor2Objects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDRedDoor2Objects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDRedDoor2Objects1[i].setAnimationName("Open");
}
}{gdjs.evtTools.sound.playSound(runtimeScene, "Audio\\door-1-open.wav", false, 100, 1);
}}

}


{

gdjs.Scene1Code.GDRedDoor3Objects1.createFrom(runtimeScene.getObjects("RedDoor3"));

gdjs.Scene1Code.condition0IsTrue_0.val = false;
gdjs.Scene1Code.condition1IsTrue_0.val = false;
{
gdjs.Scene1Code.condition0IsTrue_0.val = gdjs.evtTools.input.isMouseButtonPressed(runtimeScene, "Left");
}if ( gdjs.Scene1Code.condition0IsTrue_0.val ) {
{
gdjs.Scene1Code.condition1IsTrue_0.val = gdjs.evtTools.input.cursorOnObject(gdjs.Scene1Code.mapOfGDgdjs_46Scene1Code_46GDRedDoor3Objects1Objects, runtimeScene, true, false);
}}
if (gdjs.Scene1Code.condition1IsTrue_0.val) {
/* Reuse gdjs.Scene1Code.GDRedDoor3Objects1 */
{for(var i = 0, len = gdjs.Scene1Code.GDRedDoor3Objects1.length ;i < len;++i) {
    gdjs.Scene1Code.GDRedDoor3Objects1[i].setAnimationName("Open");
}
}{gdjs.evtTools.sound.playSound(runtimeScene, "Audio\\door-1-open.wav", false, 100, 1);
}}

}


{


{
}

}


}; //End of gdjs.Scene1Code.eventsList0xb0cf8


gdjs.Scene1Code.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();
gdjs.Scene1Code.GDHeroObjects1.length = 0;
gdjs.Scene1Code.GDHeroObjects2.length = 0;
gdjs.Scene1Code.GDRedDoorObjects1.length = 0;
gdjs.Scene1Code.GDRedDoorObjects2.length = 0;
gdjs.Scene1Code.GDRedDoor2Objects1.length = 0;
gdjs.Scene1Code.GDRedDoor2Objects2.length = 0;
gdjs.Scene1Code.GDRedDoor3Objects1.length = 0;
gdjs.Scene1Code.GDRedDoor3Objects2.length = 0;
gdjs.Scene1Code.GDUpObjects1.length = 0;
gdjs.Scene1Code.GDUpObjects2.length = 0;
gdjs.Scene1Code.GDDownObjects1.length = 0;
gdjs.Scene1Code.GDDownObjects2.length = 0;
gdjs.Scene1Code.GDTextObjects1.length = 0;
gdjs.Scene1Code.GDTextObjects2.length = 0;
gdjs.Scene1Code.GDBoxObjects1.length = 0;
gdjs.Scene1Code.GDBoxObjects2.length = 0;

gdjs.Scene1Code.eventsList0xb0cf8(runtimeScene);
return;
}
gdjs['Scene1Code'] = gdjs.Scene1Code;
