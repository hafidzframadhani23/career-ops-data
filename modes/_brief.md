# Hafidz Fadhilah Ramadhani — Triage Brief

<!-- USER LAYER. Personalized from cv.md during onboarding (2026-11-24). -->

## Identity
Civil Engineer (S.T., ITERA, IPK 3.40), ~2 yrs professional + 2 internships. Based in Pringsewu, Lampung (WIB). Indonesian citizen. BNSP Ahli Muda Teknik Bangunan Gedung.

## Target Archetypes

| # | Archetype | What they buy (your proof) |
|---|-----------|----------------------------|
| 1 | **Estimator** | RAB/BOQ/quantity take-off + AHSP for Pemprov DKI Jakarta projects, used as owner tender reference |
| 2 | **Quantity Surveyor** | Back-up quantity (concrete, formwork, rebar), BBS, RAP + Kurva S, volume checks vs contract |
| 3 | **Site Engineer** | Led Yonif TP construction in Merauke & Sorong (remote, limited logistics); shop drawing verification; manpower & logistics |
| 4 | **Infrastructure Engineer** | 87 km mining haul road: DED review, shop drawings for Box Underpass and 45 m bridge on steel pipe piles, WMS + JHSEA/IBPR |
| 5 | **Drafter** | AutoCAD, Revit (Ars/Str/MEP), InfraWorks; Revit jetty model with working drawings |

Analog titles that count as targets: Cost Engineer, Cost Control, QS Engineer, Civil Engineer, Engineer Sipil, Pelaksana, Project Engineer, Structural Drafter, Drafter Sipil, BIM Modeller.

## Proof Points
- Haul road 87 km (Kaltim): Box Underpass + 45 m span bridge, steel pipe pile foundations; BBS planned with BIM 3D to reduce rebar cut waste
- Yonif TP 806 Merauke & 801 Sorong (Kemhan RI): led site execution in remote areas
- Owner estimates (RAB, BOQ, AHSP) for Pemprov DKI Jakarta: TPS 3R, Gedung Parkir, Lapangan Olahraga, Kantor Kelurahan, Saluran Kota
- SLF structural audit of an existing factory (SAP2000, SNI 1726:2019)

## Comp Strategy
| Target | Requirement |
|--------|-------------|
| IDR 9.5-11.5 jt/month | Standard target |

**Hard floor: IDR 9.5 jt/month. Stated pay below that → FAIL regardless of other signals.** Most Indonesian postings omit salary: do not penalize a missing figure.

## Location Scoring
Preferred regions: Java (incl. Jabodetabek), Sumatra (incl. Lampung), Bali, NTB, North Sulawesi.
- On-site in a preferred region → **4.5-5.0**
- Location unstated / rotating sites → **4.0**, flag as a question
- On-site elsewhere in Indonesia (Kalimantan, other Sulawesi, NTT, Maluku, Papua) → **2.5-3.0**
- Outside Indonesia → **3.0**, flag work permit

## Hard DQ Criteria — instant FAIL (< 3.0)
- Requires 5+ years minimum experience as a hard requirement (stretch to ~3-4 years is fine)
- Senior / Manager / Lead level (Project Manager, Chief QS, Engineering Manager)
- Primary discipline outside civil (MEP/electrical/mechanical engineer, architect-only design roles)
- Requires a license/certification not held as a hard gate (e.g. SKK Madya/Utama required)

## Quick Scoring Guide

Bands are relative to `triage_threshold` (`config/profile.yml → pipeline.triage_threshold`, default **3.5**).

| Score | Verdict | What it means |
|-------|---------|---------------|
| ≥ threshold (default 3.5) | **PASS** | Archetype + location + level fit, gaps bridgeable |
| 3.0 – (threshold − 0.1) | **MARGINAL** | Borderline — shown to user as one line |
| < 3.0 | **FAIL** | Filtered |

## Soft Red Flags (−0.5 each, additive)
- Requires software not on the CV as primary tool (e.g. Tekla, Civil 3D) — check before applying
- Very short contract (< 6 months) with no extension path

## Priority Override List — always return PASS regardless of score
- (none yet)
