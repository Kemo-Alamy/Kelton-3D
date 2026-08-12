# -*- coding: utf-8 -*-
import json

ORD_AR = {1:"الأولى",2:"الثانية",3:"الثالثة",4:"الرابعة",5:"الخامسة",6:"السادسة",
          7:"السابعة",8:"الثامنة",9:"التاسعة",10:"العاشرة",11:"الحادية عشرة",12:"الثانية عشرة"}
SIDE_AR = {"r":"يمين","l":"شمال"}
GROUP_AR = {
    "skull":"الجمجمة","spine":"العمود الفقري","ribcage":"القفص الصدري","pelvis":"الحوض",
    "arm_r":"الذراع اليمين","arm_l":"الذراع الشمال","leg_r":"الرجل اليمين","leg_l":"الرجل الشمال"
}
FINGER_AR = {1:"الإبهام",2:"السبابة",3:"الوسطى",4:"البنصر",5:"الخنصر"}
TOE_AR = {1:"الإصبع الكبير",2:"إصبع القدم الثاني",3:"إصبع القدم الثالث",4:"إصبع القدم الرابع",5:"الخنصر (القدم)"}

meta = {}

def setm(key, ar, group, desc=""):
    meta[key] = {"ar": ar, "group": group, "groupAr": GROUP_AR[group], "desc": desc}

# skull
setm("skull_frontal","عظمة الجبهة","skull","تكوّن الجزء الأمامي من الجمجمة وجبهة الرأس.")
setm("skull_parietal_r","العظمة الجدارية - يمين","skull","تكوّن الجانب العلوي الجانبي للجمجمة.")
setm("skull_parietal_l","العظمة الجدارية - شمال","skull","تكوّن الجانب العلوي الجانبي للجمجمة.")
setm("skull_temporal_r","العظمة الصدغية - يمين","skull","تحيط بالأذن وتحمل جزء من عضلات المضغ.")
setm("skull_temporal_l","العظمة الصدغية - شمال","skull","تحيط بالأذن وتحمل جزء من عضلات المضغ.")
setm("skull_occipital","العظمة القذالية","skull","تكوّن مؤخرة وقاعدة الجمجمة، بها فتحة مرور الحبل الشوكي.")
setm("skull_sphenoid","العظمة الوتدية","skull","عظمة معقدة الشكل في وسط قاعدة الجمجمة.")
setm("skull_ethmoid","العظمة الغربالية","skull","تفصل تجويف الأنف عن المخ، بها فتحات صغيرة للأعصاب الشمية.")
setm("skull_zygomatic_r","عظمة الوجنة - يمين","skull","تكوّن بروز الخد.")
setm("skull_zygomatic_l","عظمة الوجنة - شمال","skull","تكوّن بروز الخد.")
setm("skull_nasal_r","عظمة الأنف - يمين","skull","تكوّن الجزء العلوي العظمي للأنف.")
setm("skull_nasal_l","عظمة الأنف - شمال","skull","تكوّن الجزء العلوي العظمي للأنف.")
setm("skull_maxilla_r","الفك العلوي - يمين","skull","يحمل الأسنان العلوية ويكوّن جزء من سقف الفم.")
setm("skull_maxilla_l","الفك العلوي - شمال","skull","يحمل الأسنان العلوية ويكوّن جزء من سقف الفم.")
setm("mandible","الفك السفلي","skull","العظمة الوحيدة المتحركة في الجمجمة، بها الأسنان السفلية.")

# spine
setm("spine_c1","الفقرة الرقبية الأولى (الأطلس)","spine","تحمل الجمجمة مباشرة وتسمح بحركة إيماء الرأس.")
setm("spine_c2","الفقرة الرقبية الثانية (المحور)","spine","تسمح بحركة استدارة الرأس يمين وشمال.")
for i in range(3,8):
    setm(f"spine_c{i}", f"الفقرة الرقبية {ORD_AR[i-2] if i-2<=12 else i}", "spine", f"الفقرة رقم {i} في منطقة الرقبة من العمود الفقري.")
for i in range(1,13):
    setm(f"spine_t{i}", f"الفقرة الصدرية {ORD_AR[i]}", "spine", f"الفقرة رقم {i} في المنطقة الصدرية، يتصل بها ضلعان.")
for i in range(1,6):
    setm(f"spine_l{i}", f"الفقرة القطنية {ORD_AR[i]}", "spine", f"الفقرة رقم {i} في أسفل الظهر، تحمل معظم وزن الجسم.")
setm("sacrum","العجز","spine","عظمة مثلثة تصل العمود الفقري بالحوض من الخلف.")

# ribcage
for i in range(1,13):
    setm(f"rib_r_{i}", f"الضلع {ORD_AR[i]} - يمين", "ribcage", f"الضلع رقم {i} من الجهة اليمين، جزء من القفص الصدري.")
    setm(f"rib_l_{i}", f"الضلع {ORD_AR[i]} - شمال", "ribcage", f"الضلع رقم {i} من الجهة الشمال، جزء من القفص الصدري.")
setm("sternum_manubrium","مقبض عظمة القص","ribcage","الجزء العلوي من عظمة القص، يتصل به الترقوتان.")
setm("sternum_body","جسم عظمة القص","ribcage","الجزء الأوسط والأكبر من عظمة القص.")
setm("sternum_xiphoid","الناتئ الخنجري","ribcage","أصغر جزء في نهاية عظمة القص السفلية.")

# pelvis
setm("hip_r","عظمة الحوض - يمين","pelvis","تحمل وزن الجسم العلوي وتصل العمود الفقري بالرجل.")
setm("hip_l","عظمة الحوض - شمال","pelvis","تحمل وزن الجسم العلوي وتصل العمود الفقري بالرجل.")

# arms
for side in ["r","l"]:
    g = f"arm_{side}"
    lbl = SIDE_AR[side]
    setm(f"clavicle_{side}", f"الترقوة - {lbl}", g, "عظمة تربط الذراع بالقفص الصدري من الأمام.")
    setm(f"scapula_{side}", f"لوح الكتف - {lbl}", g, "عظمة مثلثة مسطحة في أعلى الظهر تدعم حركة الكتف.")
    setm(f"humerus_{side}", f"عضد ال{lbl}", g, "العظمة الطويلة في أعلى الذراع بين الكتف والكوع.")
    setm(f"radius_{side}", f"الكعبرة - {lbl}", g, "إحدى عظمتي الساعد، في جهة الإبهام.")
    setm(f"ulna_{side}", f"الزند - {lbl}", g, "إحدى عظمتي الساعد، تكوّن بروز الكوع.")
    for i in range(1,6):
        setm(f"metacarpal_{side}_{i}", f"عظمة مشط اليد {ORD_AR[i]} - {lbl}", g, "عظمة مشط اليد المتصلة بأحد الأصابع.")
    for fi in range(1,6):
        fname = FINGER_AR[fi]
        if fi == 1:
            setm(f"phalanx_prox_{side}_{fi}", f"السلامية القريبة - {fname} - {lbl}", g, f"سلامية إصبع {fname} القريبة من الكف.")
            setm(f"phalanx_dist_{side}_{fi}", f"السلامية البعيدة - {fname} - {lbl}", g, f"سلامية إصبع {fname} البعيدة (طرف الإصبع).")
        else:
            setm(f"phalanx_prox_{side}_{fi}", f"السلامية القريبة - إصبع {fname} - {lbl}", g, f"سلامية إصبع {fname} القريبة من الكف.")
            setm(f"phalanx_mid_{side}_{fi}", f"السلامية الوسطى - إصبع {fname} - {lbl}", g, f"سلامية إصبع {fname} الوسطى.")
            setm(f"phalanx_dist_{side}_{fi}", f"السلامية البعيدة - إصبع {fname} - {lbl}", g, f"سلامية إصبع {fname} البعيدة (طرف الإصبع).")

# legs
for side in ["r","l"]:
    g = f"leg_{side}"
    lbl = SIDE_AR[side]
    setm(f"femur_{side}", f"عظمة الفخذ - {lbl}", g, "أطول وأقوى عظمة في جسم الإنسان.")
    setm(f"patella_{side}", f"الرضفة (عظمة الركبة) - {lbl}", g, "عظمة صغيرة مستديرة تحمي مفصل الركبة من الأمام.")
    setm(f"tibia_{side}", f"القصبة - {lbl}", g, "العظمة الكبيرة في الساق، تحمل معظم وزن الجسم.")
    setm(f"fibula_{side}", f"الشظية - {lbl}", g, "عظمة رفيعة بجانب القصبة، تساعد في الاستقرار.")
    setm(f"talus_{side}", f"عظمة الكاحل (القعقب) - {lbl}", g, "تتصل بعظمتي الساق وتحمل وزن الجسم عند الكاحل.")
    setm(f"calcaneus_{side}", f"عظمة العقب - {lbl}", g, "أكبر عظمة في القدم، تكوّن كعب القدم.")
    setm(f"navicular_{side}", f"العظمة الزورقية - {lbl}", g, "عظمة في منتصف القدم من الجهة الداخلية.")
    setm(f"cuneiform_med_{side}", f"العظمة الإسفينية الوسطى - {lbl}", g, "إحدى عظام منتصف القدم.")
    setm(f"cuneiform_int_{side}", f"العظمة الإسفينية المتوسطة - {lbl}", g, "إحدى عظام منتصف القدم.")
    setm(f"cuneiform_lat_{side}", f"العظمة الإسفينية الجانبية - {lbl}", g, "إحدى عظام منتصف القدم.")
    setm(f"cuboid_{side}", f"العظمة المكعبة - {lbl}", g, "عظمة في الجهة الخارجية لمنتصف القدم.")
    for i in range(1,6):
        setm(f"metatarsal_{side}_{i}", f"عظمة مشط القدم {ORD_AR[i]} - {lbl}", g, "عظمة مشط القدم المتصلة بأحد أصابع القدم.")
    for ti in range(1,6):
        tname = TOE_AR[ti]
        if ti == 1:
            setm(f"toe_phalanx_prox_{side}_{ti}", f"السلامية القريبة - {tname} - {lbl}", g, f"سلامية {tname} القريبة.")
            setm(f"toe_phalanx_dist_{side}_{ti}", f"السلامية البعيدة - {tname} - {lbl}", g, f"سلامية {tname} البعيدة.")
        else:
            setm(f"toe_phalanx_prox_{side}_{ti}", f"السلامية القريبة - {tname} - {lbl}", g, f"سلامية {tname} القريبة.")
            setm(f"toe_phalanx_mid_{side}_{ti}", f"السلامية الوسطى - {tname} - {lbl}", g, f"سلامية {tname} الوسطى.")
            setm(f"toe_phalanx_dist_{side}_{ti}", f"السلامية البعيدة - {tname} - {lbl}", g, f"سلامية {tname} البعيدة.")

bones = json.load(open("/home/claude/bone_list.json", encoding="utf-8"))
found_keys = {b["key"] for b in bones}
missing_meta = found_keys - set(meta.keys())
extra_meta = set(meta.keys()) - found_keys
print("missing meta for found bones:", missing_meta)
print("meta entries with no matching bone (ok, e.g. toe_1 fallback):", len(extra_meta))

out = {k: meta[k] for k in found_keys if k in meta}
print("final meta entries:", len(out))
json.dump(out, open("/home/claude/bone_meta.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
