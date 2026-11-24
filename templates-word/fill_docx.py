import docx, copy, sys, json
from docx.oxml.ns import qn
FMT=sys.argv[1]; OUT=sys.argv[2]; spec=json.load(open(sys.argv[3]))

def drop(el): el.getparent().remove(el)
def set_text(p, text):
    rs=p.runs
    for h in p._p.findall(qn('w:hyperlink')): drop(h)
    for r in rs[1:]: drop(r._r)
    rs[0].text=text
def set_plain_keep_links(p, text):
    # replace plain runs before the first hyperlink with one run; keep hyperlink(s)
    rs=p.runs
    for r in rs[1:]: drop(r._r)
    rs[0].text=text
def set_link_text(p, text):
    for h in p._p.findall(qn('w:hyperlink')):
        ts=list(h.iter(qn('w:t')))
        ts[0].text=text
        for t in ts[1:]: t.text=''
def set_bullets(paras, texts):
    tmpl=paras[-1]._p
    for p,t in zip(paras,texts): set_text(p,t)
    for p in paras[len(texts):]: drop(p._p)
    last=paras[min(len(texts),len(paras))-1]._p
    for t in texts[len(paras):]:
        new=copy.deepcopy(tmpl); last.addnext(new); last=new
        from docx.text.paragraph import Paragraph
        set_text(Paragraph(new,paras[0]._parent),t)

# ---------------- CV ----------------
d=docx.Document(f"{FMT}/cv.docx"); P=list(d.paragraphs); c=spec['cv']
set_text(P[2],c['summary'])
set_text(P[3],"KEY SKILLS"); set_bullets(P[4:10],c['skills'])
set_text(P[10],"WORK EXPERIENCE")
set_text(P[11],"PT. Lancarjaya Mandiri Abadi – Infrastructure Engineer (Contract)")
set_text(P[12],"Nusaraya Project 1A, Haul Road Construction (87 km), East Kalimantan\tJune 2026 – Present")
set_bullets(P[13:18],c['lj'])
set_text(P[18],"PT. Andromega Buana Abadi – Site Engineer (Full-Time)")
set_text(P[19],"Yonif TP 806 Merauke & Yonif TP 801 Sorong Project, Ministry of Defence RI\tAugust 2025 – June 2026")
set_bullets(P[20:25],c['ab'])
set_text(P[25],"PT. Istana Kreasi Indah Cipta – Estimator (Full-Time)\tNovember 2024 – July 2025")
set_bullets(P[26:30],c['ik'])
set_text(P[30],"CONSULTANT PROJECT EXPERIENCE")
set_text(P[31],"Structural Audit of an Existing Factory Building (SLF Issuance)\tMarch – May 2024")
set_text(P[32],"With a multidisciplinary team, inspected an existing factory building and assessed its structural adequacy through field observation, material testing and SAP2000 analysis in accordance with SNI 1726:2019.")
set_text(P[33],"Wastewater Treatment Plant (IPAL) Building\tFebruary – April 2024")
set_text(P[34],c.get('ipal',"Assessed the building requirements, then prepared the structural analysis, engineering drawings, 3D model and cost estimate, and supervised the work on site."))
set_text(P[35],"Jetty Extension in a Factory Area, Teluk Betung, Lampung\tApril – May 2024")
set_text(P[36],"Modelled the extension of the existing jetty in Revit and prepared working drawings, sections and structural details.")
set_text(P[37],"INTERNSHIP EXPERIENCE")
set_text(P[38],"PT. Hutama Karya – Intern, Toll Road Operations & Maintenance")
set_text(P[39],"Terbanggi Besar – Pematang Panggang – Kayu Agung Toll Road Section\tAugust – December 2021")
set_bullets(P[40:42],["Took part in maintenance and repair activities on a 112 km toll road, including field condition inspections.","Prepared monthly toll road operations reports covering maintenance, repairs and toll revenue."])
set_text(P[42],"PT. Wijaya Karya – Quality Control Assistant")
set_text(P[43],"PIK 2 Bridge Construction Project, Tangerang\tJune – July 2021")
set_bullets(P[44:46],c['wk'])
set_text(P[46],"EDUCATION & CERTIFICATION")
r=P[47].runs; r[0].text="Bachelor of Civil Engineering (Sarjana Teknik Sipil) | "; 
for x in r:
    if x.text=="Ijazah & Transkrip": x.text="Diploma & Transcript"
set_text(P[48],"Institut Teknologi Sumatera – GPA: 3.40\tSouth Lampung, Lampung")
set_plain_keep_links(P[49],"Ahli Muda Teknik Bangunan Gedung (Junior Building Engineering Expert) | "); set_link_text(P[49],"Certificate")
set_text(P[51],"ITERA English Proficiency Test (InciTe) – Score 550\tSeptember 2024")
set_text(P[52],"Language Centre (UPT Bahasa), Institut Teknologi Sumatera")
set_text(P[53],"COURSES & TRAINING")
for i,t in [(54,"Sipilpedia Academy: Microsoft Project for Scheduling and Controlling – "),(57,"Sipilpedia Academy: Revit Complete Project (Architecture-Structure-MEP) – "),(58,"Sipilpedia Academy: Revit for Infrastructure (Box Girder, Truss Bridge, Underpass, Box Culvert) – "),(59,"Langen Teknik Satria: Preparing RAP, RAB and BOQ in Civil Construction – ")]:
    set_plain_keep_links(P[i],t); set_link_text(P[i],"Certificate")
set_text(P[55],"Sipilpedia Academy: Steel Structure Modelling and Detailing with Autodesk Advance Steel (Case Studies: Warehouse & Steel Bridge)")
set_text(P[56],"TakeClass: Plaxis 2D V20 – Embankment Analysis")
if c.get('course_first')==59:
    P[54]._p.addprevious(P[59]._p)
set_text(P[60],"ORGANIZATIONS & VOLUNTEERING")
set_text(P[61],"Chairperson, UKM MADANI ITERA\tNovember 2020 – January 2022")
set_text(P[62],"Led an organization of more than 50 members across 7 divisions, coordinating cross-division planning and delivery of work programs.")
set_text(P[63],"Public Relations Communication, World Cleanup Day (WCD) Lampung\tJune – September 2020")
set_text(P[64],"Built partnerships with media, sponsors and government agencies to mobilize more than 164,000 volunteers and collect more than 109,000 kg of waste across Lampung Province.")
d.core_properties.title="CV - Hafidz Fadhilah Ramadhani"
d.save(f"{OUT}/{spec['cv_name']}.docx")

# ---------------- Cover letter ----------------
d=docx.Document(f"{FMT}/cl.docx"); T=d.tables[0]; L=spec['cl']
cell=T.cell(0,1); set_text(cell.paragraphs[0],"24 November 2026")
set_text(T.cell(2,0).paragraphs[0],"To:")
set_text(T.cell(3,0).paragraphs[0],L['to1'])
set_text(T.cell(4,0).paragraphs[0],L['to2'])
set_text(T.cell(6,0).paragraphs[0],"Dear Hiring Manager,")
set_text(T.cell(8,0).paragraphs[0],L['p1'])
cp=T.cell(10,0).paragraphs
set_text(cp[0],"Key competencies I can contribute:")
set_bullets(cp[1:6],L['points'])
set_text(T.cell(12,0).paragraphs[0],L['gap'])
set_text(T.cell(14,0).paragraphs[0],L['close'])
sp=T.cell(16,0).paragraphs; set_text(sp[0],"Sincerely,")
d.core_properties.title="Cover Letter - Hafidz Fadhilah Ramadhani"
d.save(f"{OUT}/{spec['cl_name']}.docx")
print("saved")
