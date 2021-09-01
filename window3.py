import pymel.core as pm

def window3(ws):
    rad = ws['fl1'].getValue()
    num = ws['it1'].getValue()
    ix = ws['fl2'].getValue()
    iy = ws['fl3'].getValue()
    r = 0.0
    ty = 0.0
    for i in range(num):
        name = pm.circle()
        name[0].tx.set(rad)
        pm.rotate([0, r, 0],ws=True, p=[0, 0, 0])
        name[0].ty.set(ty)
        r += 30.0 
        ty += iy
        rad += ix
    pm.select (all=True)
    pm.loft()
    
def makeWindow():
    with pm.window():
        with pm.autoLayout():
            ws = {}
            ws["it1"] = pm.intSliderGrp(label="å¬êî", field=True, min=0, max=100, value=30)
            ws["fl1"] = pm.floatSliderGrp(label="îºåa", field=True, min=0.0, max=10.0, value=5.0)
            ws["fl2"] = pm.floatSliderGrp(label="ëùå∏ílX", field=True, min=-1.0, max=1.0, value=-0.1)
            ws["fl3"] = pm.floatSliderGrp(label="ëùå∏ílY", field=True, min=0.0, max=1.0, value=0.3)
            pm.button(label="ÇŒÇÀçÏê¨", command=pm.Callback(window3, ws))
            
makeWindow()