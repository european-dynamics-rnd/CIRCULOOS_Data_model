# Data Model Clustering

Survey of all 37 `schema.json` files in this repo, grouped by semantic role rather than by folder/openCall. Goal: spot where different openCalls independently reinvented the same entity shape, as candidates for a shared base schema.

## Clusters

### 1. Physical Material / Substance spec
Raw material properties, no batch/lot identity. This is the one cluster with cross-openCall, non-domain-specific base schemas already living under `material/` — every other cluster in this doc is openCall-scoped.
- `material/leather` — origin, color, thickness, tannedProcess, hardness, recycledTimes
- `material/wood` — species, density, moistureContent, tensile/compressive/bending strength, thermalConductivity
- `material/plastic` — polymerType, meltFlowIndex, recycledContent, moldTemperature/shrinkage figures, batchNumber
- `openCallSpecific/biocorner/SRM` — category, chemicalComposition, density, pretreatmentRequired, storageConditions

Terminology note: SRM ("Secondary Raw Material") and "Recyclate" name the same underlying idea — material born from recycling, not virgin/nature. SRM frames it relative to virgin material (a substitution comparison); Recyclate names the recycling process's output directly. No repo schema currently uses the word Recyclate, but the material tracked loop-over-loop in `openCallSpecific/shineagain/MaterialRecord` (via `Material_Loop`) is conceptually the same thing under a third name.

`material/plastic` already carries a `recycledContent` field — the generic base schema for exactly the kind of material `openCallSpecific/esp_islopol/EPSBatch` (expanded polystyrene, a plastic) tracks, but EPSBatch doesn't derive from or reference it (see reinvented table below).

### 2. Batch / Lot
Traceable quantity of material moving through a chain.
- `openCallSpecific/biocorner/MortarBatch`
- `openCallSpecific/biocorner/SRMBatch`
- `openCallSpecific/esp_islopol/EPSBatch`
- `openCallSpecific/yeast/YeastBatch`
- `openCallSpecific/biomass_evop/BiomassInventory` (stock-position variant)

### 3. Product / Product Model
Catalog-level or finished-item definition.
- `openCallSpecific/biocorner/MortarProduct`
- `openCallSpecific/esp_islopol/ProductModel`
- `openCallSpecific/esp_islopol/Product`
- `openCallSpecific/yeast/YeastProduct`
- `openCallSpecific/stainless_steel_dpp` (digital product passport)
- `processes/3D_print_concrete` (reConcretePart)

### 4. Recipe / Formulation
- `openCallSpecific/biocorner/Recipe`

### 5. Process — definition vs execution
- Definition: `openCallSpecific/biocorner/Process`, `openCallSpecific/esp_islopol/Process`
- Execution/event: `openCallSpecific/esp_islopol/ProcessEvent`, `openCallSpecific/esp_islopol/ProductionRun`, `openCallSpecific/shineagain/MaterialRecord` (process-step side — see note in cluster 8)

### 6. Sensor / IoT observation
Real-time machine monitoring.
- `openCallSpecific/electrospindle_machine_iot` (Iot_UV5)
- `openCallSpecific/granular_printers/3DPrintingProcess`
- `openCallSpecific/plasmix_road/ExtruderObservation`
- `openCallSpecific/biomass_evop/BoilerTestSession`

### 7. Automated measurement / inspection / QC result
- `openCallSpecific/esp_islopol/EPSObservation`
- `openCallSpecific/esp_islopol/EPSVisualInspection`
- `openCallSpecific/searcle/SEMImage`

### 8. Transport / Logistics / Movement event
- `openCallSpecific/esp_islopol/EPSTransport`
- `openCallSpecific/esp_islopol/RecyclingMaterialCollection`
- `openCallSpecific/biomass_evop/BiomassStockMovement`
- `openCallSpecific/shineagain/MaterialRecord` (transport side — see note below)

`shineagain/MaterialRecord` is a hybrid: one schema covers both a process step (`Proces_step`, `Material_in_kg`/`Material_out_kg`, `Energy_use_kWh`) and a transport leg (`Start_location`, `End_location`, `Type_of_transport`, `KM`), distinguished only by which fields are populated. Every other openCall split these into separate entities (cluster 5 vs cluster 8) — this is a third pattern: one flexible record type instead of two strict ones.

### 9. Actor / Organization
- `openCallSpecific/biocorner/Organization`
- `openCallSpecific/biocorner/Supplier`
- `openCallSpecific/yeast/Company`

### 10. Facility / Site
- `openCallSpecific/esp_islopol/Factory`

### 11. Asset — Vehicle
- `openCallSpecific/esp_islopol/Vehicle`
- `openCallSpecific/esp_islopol/VehicleModel`

### 12. Certification / Compliance document
- `openCallSpecific/biocorner/DoP`

### 13. Marketplace / Offer / Commercial listing
- `openCallSpecific/biomass_evop/MaterialOffer`
- `intra-communication` (material ad, free-text type — no fixed enum)

### 14. Environmental / Sustainability indicator
- `sustainabilityIndicators` (environmental_footprint_indicator)

### 15. Generic building/spatial template (outlier)
- `template/schema.json` (`Storey`, `Room`) — Smart Data Models base template, not domain-specific

## What's reinvented across openCalls

Each openCall folder independently modeled the same handful of roles, with different field names and no shared parent schema:

| Role | Reinvented in | Divergent field names for same concept |
|---|---|---|
| Batch/Lot | biocorner (MortarBatch, SRMBatch), esp_islopol (EPSBatch), yeast (YeastBatch) | `batchCode` vs `runId`/`batchId` for batch identity; each defines its own origin/quantity/status fields from scratch |
| Organization/Actor | biocorner (Organization, Supplier), yeast (Company) | `role`/`supplyChainRole`/`tier` (biocorner) vs `valueChainRole`/`category` (yeast) — same concept, no shared vocabulary |
| Process definition | biocorner (Process), esp_islopol (Process) | Both define a bare process-template entity independently |
| Process execution | esp_islopol (ProcessEvent, ProductionRun), shineagain (MaterialRecord) | Two separate entities in the same openCall for what looks like the same concept (event vs run); shineagain folds this into one flexible record instead |
| Product | biocorner (MortarProduct), esp_islopol (Product, ProductModel), yeast (YeastProduct) | Each has its own product/product-model split or lack thereof |
| Transport/movement | esp_islopol (EPSTransport, RecyclingMaterialCollection), biomass_evop (BiomassStockMovement), shineagain (MaterialRecord) | Four separate shapes for "material moved from A to B at time T" |
| Sensor/IoT observation | electrospindle_machine_iot, granular_printers, plasmix_road, biomass_evop (BoilerTestSession) | Each is a flat bag of machine-specific sensor fields, no shared "timestamp + device + readings[]" base |
| Material spec | `material/leather`, `material/wood`, `material/plastic` (shared, generic), biocorner (SRM) | `material/` already generalizes this role; SRM re-derives its own category/composition/density fields instead of extending `material/plastic` or a shared base; `esp_islopol/EPSBatch` (a plastic) doesn't reference `material/plastic` either |

## Suggested next step

Introduce shared abstract base schemas (e.g. under a new `shared/` or existing `material/`, `processes/` folders) for: **Batch**, **Organization**, **Process**, **ProcessEvent**, **TransportMovement**, **SensorObservation** — reused via `allOf` by each openCall, instead of duplicating the shape per openCall. `material/` is the one place this pattern already exists (leather, wood, plastic); extend the same approach to SRM and to plastic-family batches (EPSBatch) rather than adding a fourth. Not done in this pass; flagging only.
