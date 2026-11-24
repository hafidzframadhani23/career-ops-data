import json,sys
S=sys.argv[1]
SK={
"assess":"Structural Assessment: Existing Structure Inspection, Material Testing, Structural Analysis to SNI 1726:2019 (SAP2000, ETABS), Building Functional Worthiness Evaluation (SLF)",
"docs":"Technical Documents: DED & Shop Drawing Review, Technical Specifications, Bar Bending Schedule (BBS), Back-Up Quantity, Technical Justification",
"cost":"Cost & Feasibility: RAB/RAP, BOQ, Unit Price Analysis (AHSP), S-Curve Scheduling",
"k3":"K3 (OHS) & Environment: Work Method Statement (WMS), JHSEA, Hazard Identification & Risk Assessment (IBPR), Field Inspection",
"sw":"Software: AutoCAD, Revit (Architecture, Structure, MEP), SAP2000, ETABS, InfraWorks, Microsoft Office Suite (Excel, Word)",
"lang":"Languages: Indonesian, English (ITERA English Proficiency Test: 550)"}
LJ={"ded":"Reviewed DED and prepared shop drawings for the main structures of a mining haul road, a Box Underpass and a 45 m span bridge on Steel Pipe Pile foundations, so that details matched the design criteria and actual field conditions.",
"bbs":"Prepared Bar Bending Schedules (BBS) and reduced rebar cutting waste by planning cut lengths through 3D BIM modelling before fabrication.",
"wms":"Prepared Work Method Statements (WMS) for structural works, from procurement and mobilization through main works to sundries & finishing, complete with JHSEA and IBPR so hazards and controls were set before work began.",
"qty":"Calculated back-up quantities for concrete, formwork & reinforcement, and compiled material, equipment and labor resource requirements.",
"insp":"Carried out field inspections and progress monitoring, and prepared technical justifications for field issues as the basis for decisions by the Engineering Manager and Owner."}
AB={"lead":"Led the construction of Yonif TP (Territorial Development Infantry Battalion) facilities in remote areas with limited access and logistics.",
"verify":"Verified shop drawings and technical specifications before execution, then supervised each stage for compliance with specifications and schedule.",
"rap":"Prepared the RAP (cost budget) and S-curve as the reference for cost and progress control.",
"log":"Managed manpower and set logistics and material procurement strategies to keep supplies flowing at remote sites.",
"coord":"Coordinated with the supervision consultant, subcontractors, the Indonesian Army (TNI) and government agencies to resolve technical and operational issues."}
IK={"rab":"Prepared RAB, BOQ and independent quantity take-offs for DKI Jakarta Provincial Government projects, including a TPS 3R waste facility, a parking building, a sports field, a sub-district office and city drainage.",
"ahsp":"Prepared Unit Price Analyses (AHSP) based on current material and labor prices; the owner used the results as the reference for tender and procurement values.",
"sup":"Also served as the owner's field supervisor, monitoring contractor work against working drawings, technical specifications and contract volumes.",
"svy":"Conducted site surveys to verify existing conditions as the basis for volume and cost calculations."}
WK={"pile":"Supervised pile driving and pile testing (calendering & PDA Test), concrete casting and on-site concrete quality testing.",
"rebar":"Checked and calculated bridge rebar work against the shop drawings."}

ega={"cv_name":"CV_Hafidz_Fadhilah_Ramadhani_Civil_Engineer_Ega_Tekelindo_Prima","cl_name":"Cover_Letter_Hafidz_Fadhilah_Ramadhani_Civil_Engineer_Ega_Tekelindo_Prima",
"cv":{"summary":"Civil Engineering graduate of Institut Teknologi Sumatera (ITERA) with ±2 years of professional experience on both the consultant/owner and contractor sides. Currently handling structural works on an 87 km mining haul road in East Kalimantan: DED review, shop drawings, Bar Bending Schedules, back-up quantities, and Work Method Statements with K3 analysis (JHSEA & IBPR). Previously led the construction of Yonif TP facilities in remote Merauke and Sorong, prepared owner cost estimates for government projects, and took part in a structural audit of an existing factory for SLF issuance. BNSP-certified Ahli Muda Teknik Bangunan Gedung. Seeking to grow in civil construction supervision, including mine infrastructure projects.",
 "skills":[SK["docs"],SK["k3"],SK["cost"],SK["assess"],SK["sw"],SK["lang"]],
 "lj":[LJ["ded"],LJ["insp"],LJ["qty"],LJ["bbs"],LJ["wms"]],
 "ab":[AB["lead"],AB["verify"],AB["log"],AB["rap"],AB["coord"]],
 "ik":[IK["sup"],IK["rab"],IK["ahsp"],IK["svy"]],
 "wk":[WK["pile"],WK["rebar"]]},
"cl":{"to1":"Hiring Manager, PT Ega Tekelindo Prima","to2":"Tangerang, Banten",
 "p1":"I am writing to apply for the Civil Engineer (Project Supervisor) position at PT Ega Tekelindo Prima. I hold a Bachelor's degree in Civil Engineering from Institut Teknologi Sumatera (GPA 3.40) and the BNSP Ahli Muda Teknik Bangunan Gedung certification. I am currently an Infrastructure Engineer on an 87 km mining haul road project in East Kalimantan, and before that I led the construction of Yonif TP facilities in Merauke and Sorong as a Site Engineer. Your note that mine infrastructure experience is a plus describes the work I do today.",
 "points":["Mine infrastructure: reviewing DED and preparing shop drawings for haul road structures, a Box Underpass and a 45 m span bridge on Steel Pipe Pile foundations, and checking them against actual field conditions.",
  "Site supervision and project reports: field inspections, progress monitoring and technical justifications for the Engineering Manager and Owner; at Yonif TP, supervising each construction stage against specifications and schedule.",
  "Material requirements: calculating back-up quantities for concrete, formwork and reinforcement, compiling material, equipment and labor needs, and preparing RAP and S-curves for cost and progress control.",
  "Drawings and standards: AutoCAD and Revit for engineering drawings, 3D BIM modelling to plan rebar cutting, and structural analysis to SNI 1726:2019 with SAP2000 and ETABS.",
  "Ready for site placement: I have worked on projects in Merauke, Sorong and East Kalimantan, and I am willing to be placed in Tangerang, Sumatra or Kalimantan."],
 "gap":"My work on the haul road has focused on its structures rather than on cut and fill earthworks, so that is the part of the role I would build on the job, alongside the volume and site experience I already have. My English score comes from the ITERA English Proficiency Test (550), and I am ready to take a TOEFL ITP if required.",
 "close":"Thank you for your time and consideration. I would welcome the opportunity to discuss how I can contribute to your projects."}}

tak={"cv_name":"CV_Hafidz_Fadhilah_Ramadhani_Estimator_Takenaka_Indonesia","cl_name":"Cover_Letter_Hafidz_Fadhilah_Ramadhani_Estimator_Takenaka_Indonesia",
"cv":{"summary":"Civil Engineering graduate of Institut Teknologi Sumatera (ITERA) with ±2 years of professional experience on both the owner and contractor sides, focused on quantities and cost. As an Estimator, prepared RAB, BOQ, independent quantity take-offs and Unit Price Analyses (AHSP) for DKI Jakarta Provincial Government building projects, which the owner used as the reference for tender and procurement values. Since then, on site, prepared the RAP and S-curve for cost and progress control, back-up quantities for concrete, formwork and reinforcement, and Bar Bending Schedules, while reviewing DED, shop drawings and technical specifications. BNSP-certified Ahli Muda Teknik Bangunan Gedung. Seeking to grow as an Estimator / Quantity Surveyor in building construction.",
 "skills":[SK["cost"].replace("Cost & Feasibility: ","Cost & Estimating: Quantity Take-Off, "),SK["docs"],SK["sw"],SK["assess"],SK["k3"],SK["lang"]],
 "lj":[LJ["qty"],LJ["bbs"],LJ["ded"],LJ["wms"],LJ["insp"]],
 "ab":[AB["rap"],AB["verify"],AB["log"],AB["coord"],AB["lead"]],
 "ik":[IK["rab"],IK["ahsp"],IK["svy"],IK["sup"]],
 "wk":[WK["rebar"],WK["pile"]],
 "course_first":59},
"cl":{"to1":"Hiring Manager, PT Takenaka Indonesia","to2":"Jakarta",
 "p1":"I am writing to apply for the Estimator position at PT Takenaka Indonesia. I hold a Bachelor's degree in Civil Engineering from Institut Teknologi Sumatera (GPA 3.40) and the BNSP Ahli Muda Teknik Bangunan Gedung certification. As an Estimator at PT Istana Kreasi Indah Cipta, I prepared quantity take-offs, BOQs and unit price analyses for DKI Jakarta Provincial Government building projects, and I have since continued working on quantities and cost from the contractor side.",
 "points":["Quantity take-off and BOQ: independent take-offs, RAB and BOQ for building and civil projects, including a parking building, a TPS 3R waste facility, a sports field, a sub-district office and city drainage.",
  "Unit rate analysis: AHSP built from current material and labor prices; the owner used my results as the reference for tender and procurement values.",
  "Reading drawings and specifications: reviewing DED, shop drawings and technical specifications, and verifying existing site conditions before calculating volumes.",
  "Contractor-side quantities and cost control: back-up quantities for concrete, formwork and reinforcement, Bar Bending Schedules, and RAP and S-curves.",
  "Tools: proficient in Microsoft Excel and Word for estimates and reports, and in AutoCAD and Revit for reading and modelling drawings."],
 "gap":"I have not yet used Cubicost; my take-offs so far have been done with AutoCAD and Excel, and I am ready to learn Cubicost quickly. My time with the Estimator title is about nine months, backed by more than a year of quantity and cost work on site since then.",
 "close":"Thank you for your time and consideration. I would welcome the opportunity to discuss how I can contribute to your estimating team."}}
for n,s in (("ega",ega),("tak",tak)): json.dump(s,open(f"{S}/spec-{n}.json","w"),ensure_ascii=False,indent=1)
