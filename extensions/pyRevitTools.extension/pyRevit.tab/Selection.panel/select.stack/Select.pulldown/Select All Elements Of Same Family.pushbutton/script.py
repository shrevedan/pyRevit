from pyrevit.framework import List
from pyrevit import revit, DB, UI


matchlist = []

selection = revit.get_selection()

for el in selection:
    try:
        family = el.Symbol.Family
        symbolIdSet = family.GetFamilySymbolIds()
        for symid in symbolIdSet:
            cl = DB.FilteredElementCollector(revit.doc)\
                   .WherePasses(DB.FamilyInstanceFilter(revit.doc, symid))\
                   .ToElements()
            for el in cl:
                matchlist.append(el.Id)
    except Exception:
        continue

selSet = []
for elid in matchlist:
    selSet.append(elid)

selection.set_to(selSet)
revit.uidoc.RefreshActiveView()
