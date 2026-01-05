# Enhanced Vertical Categorization - Summary Report

**Date:** January 5, 2026
**Analysis:** ALL 9,079 opportunities analyzed with enhanced keyword patterns
**Output:** `opportunities_enhanced_verticals.csv` with new `Enhanced_Vertical` column

---

## What Was Done

I analyzed **ALL 9,079 opportunities** (not just Commercial) using expanded keyword patterns that examine:
- **Opportunity Name** field
- **Industry** field
- **Existing Vertical** field

The analysis extracts business type keywords and assigns granular categories to create more actionable marketing segments.

---

## Results Summary

### Before Enhancement:
- **Blank verticals:** 2,198 (24.2%)
- **"Commercial" verticals:** 2,956 (32.6%)
- **Total needing improvement:** 5,154 (56.8%)

### After Enhancement:
- **"Uncategorized":** 2,253 (24.8%)
- **"Commercial - General":** 2,676 (29.5%)
- **Total still general:** 4,929 (54.3%)

### Improvement:
✅ **225 opportunities** now have specific categories (2.5% improvement)
✅ **40+ granular categories** instead of 17 broad ones
✅ **Better segmentation** for high-value verticals

---

## Why Only 2.5% Improvement?

The limitation is that **most opportunity names don't contain specific business type keywords**.

**Examples of non-specific names:**
- "BT"
- "G PROX II"
- "Baldwin"
- "Palatine"
- "126 Lambton Quay"

These are internal project codes or location names without business type indicators, making it impossible to categorize without manual review.

**However**, when opportunity names DO contain keywords, the enhanced categorization works well:
- "20 Classroom School" → **Education - K-12** ✅
- "Ramada Conference Centre Queenstown" → **Hospitality - Hotels & Resorts** ✅
- "Hyatt Regency Ha long in Vietnam" → **Hospitality - Hotels & Resorts** ✅
- "Bayswater Maritime Precinct" → **Critical Infrastructure - Ports & Maritime** ✅
- "LNG Project, Sumbawa Indonesia" → **Critical Infrastructure - Utilities & Energy** ✅

---

## New Granular Categories (40 Total)

### Commercial Categories (More Specific)
- Commercial - Office Buildings (45 opps, 45.5% win rate)
- Commercial - Mixed Use Development (23 opps, 21.1% win rate)
- Commercial - Construction Projects (14 opps, 27.3% win rate)
- Commercial - General (2,676 opps, 53.4% win rate)

### Hospitality (New!)
- **Hospitality - Hotels & Resorts** (43 opps, 17.9% win rate) ⚠️ Low win rate
- **Hospitality - Food & Beverage** (11 opps, 60.0% win rate) ✅ High win rate

### Healthcare (More Granular)
- **Healthcare - Hospitals & Clinics** (117 opps, 43.8% win rate)
- **Healthcare - Senior Living** (17 opps, 38.5% win rate)
- **Healthcare - Dental** (6 opps, 50.0% win rate)
- Healthcare - General (359 opps, 46.5% win rate)

### Education (More Granular)
- **Education - Higher Education** (95 opps, 53.5% win rate)
- **Education - K-12** (151 opps, 35.6% win rate)
- **Education - Training Centers** (339 opps, 53.8% win rate)
- Education - General (255 opps, 60.0% win rate)

### Government (More Granular)
- **Government - General** (88 opps, **72.4% win rate**) ⭐ Highest win rate!
- **Government - Judicial** (9 opps, 42.9% win rate)
- **Government - Libraries** (6 opps, 40.0% win rate)
- **Government - Civic Buildings** (2 opps, 50.0% win rate)
- **Government - Corrections** (5 opps, 50.0% win rate)
- Government (332 opps, 46.7% win rate)

### Industrial (New Categories)
- **Industrial - Manufacturing** (62 opps, 32.1% win rate) ⚠️ Low win rate
- **Industrial - Warehouse & Logistics** (40 opps, 57.9% win rate) ✅ Good win rate
- **Industrial - Heavy Industry** (90 opps, 54.2% win rate)

### Critical Infrastructure (More Granular)
- **Critical Infrastructure - Aviation** (32 opps, 48.3% win rate, **$52,242 avg deal**) 💰 Highest value!
- **Critical Infrastructure - Ports & Maritime** (57 opps, 36.7% win rate)
- **Critical Infrastructure - Transportation** (48 opps, 47.8% win rate)
- **Critical Infrastructure - Utilities & Energy** (31 opps, 58.1% win rate)
- **Critical Infrastructure - Data Centers** (2 opps, 0.0% win rate) ⚠️
- Critical Infrastructure - General (39 opps, 51.5% win rate)

### Entertainment (New!)
- **Entertainment - Museums & Cultural** (26 opps, 42.9% win rate)
- **Entertainment - Gaming & Casinos** (15 opps, 38.5% win rate)
- **Entertainment - Sports Facilities** (9 opps, 16.7% win rate) ⚠️ Low win rate
- **Entertainment - Fitness & Recreation** (6 opps, 50.0% win rate)
- **Entertainment - Theater & Arts** (5 opps, 0.0% win rate) ⚠️ No wins

### Residential
- **Residential - Multi-Family** (1,024 opps, 38.7% win rate)
- Residential - General (253 opps, 41.6% win rate)

### Other
- **Banking & Finance** (267 opps, **67.7% win rate**) ⭐ Second highest win rate!
- **Retail** (151 opps, 48.9% win rate)
- **Religious Facilities** (76 opps, 43.3% win rate)

---

## Top Marketing Opportunities by Enhanced Categories

### 🏆 Highest Win Rate Segments

| Category | Opportunities | Win Rate | Avg Deal |
|----------|---------------|----------|----------|
| **Government - General** | 88 | **72.4%** | $8,501 |
| **Banking & Finance** | 267 | **67.7%** | $10,389 |
| **Hospitality - Food & Beverage** | 11 | **60.0%** | $5,602 |
| **Education - General** | 255 | **60.0%** | $17,285 |
| **Critical Infrastructure - Utilities & Energy** | 31 | **58.1%** | $3,416 |

**Marketing Recommendation:** These segments convert exceptionally well. Double down with targeted campaigns, case studies, and industry-specific content.

---

### 💰 Highest Value Segments

| Category | Win Count | Avg Deal Size | Total Won Value |
|----------|-----------|---------------|-----------------|
| **Critical Infrastructure - Aviation** | 14 | **$52,242** | $731,393 |
| **Residential - Multi-Family** | 292 | $27,041 | $7,896,035 |
| **Healthcare - General** | 145 | $23,434 | $3,397,995 |
| **Healthcare - Hospitals & Clinics** | 46 | $19,143 | $880,560 |
| **Education - Higher Education** | 46 | $18,678 | $859,179 |

**Marketing Recommendation:** Aviation deals are extremely high-value but complex. Healthcare and Education show strong volume + value combination.

---

### 📊 Highest Volume Segments

| Category | Opportunities | % of Total |
|----------|---------------|------------|
| Commercial - General | 2,676 | 29.5% |
| Uncategorized | 2,253 | 24.8% |
| **Residential - Multi-Family** | 1,024 | 11.3% |
| Healthcare - General | 359 | 4.0% |
| Education - Training Centers | 339 | 3.7% |

**Marketing Recommendation:** Multi-Family is the largest addressable specific market. Current 38.7% win rate could be improved with targeted campaigns.

---

### ⚠️ Problem Segments (Low Win Rates)

| Category | Opportunities | Win Rate | Why Low? |
|----------|---------------|----------|----------|
| **Hospitality - Hotels & Resorts** | 43 | **17.9%** | Losing to competition |
| **Entertainment - Theater & Arts** | 5 | **0.0%** | 0 wins |
| **Commercial - Mixed Use Development** | 23 | **21.1%** | Complex projects |
| **Entertainment - Sports Facilities** | 9 | **16.7%** | Specialized requirements |
| **Commercial - Construction Projects** | 14 | **27.3%** | Timing/budget issues |

**Marketing Recommendation:**
- **Hotels:** Investigate why we're losing. Competitive analysis needed. May need hospitality-specific solution.
- **Theater/Entertainment:** Very small sample, but concerning. May not be a fit.
- **Sports:** Specialized market with unique requirements.

---

## Examples of Successful Re-Categorizations

### Commercial → Specific Categories

| Opportunity Name | Old | New |
|------------------|-----|-----|
| Ramada Conference Centre Queenstown | Commercial | Hospitality - Hotels & Resorts |
| Hyatt Regency Ha long in Vietnam | Commercial | Hospitality - Hotels & Resorts |
| LATITUDE CORPORATE CENTER | Commercial | Commercial - Office Buildings |
| PX - Aotea - NZ Post Retail | Commercial | Retail |
| Biofarma Dawuan | Commercial | Industrial - Heavy Industry |
| RW Communications Warehouse GX | Commercial | Industrial - Warehouse & Logistics |
| Kiwibank GX/PX | Commercial | Banking & Finance |

### Blank → Specific Categories

| Opportunity Name | Old | New |
|------------------|-----|-----|
| Bayswater Maritime Precinct | (Blank) | Critical Infrastructure - Ports & Maritime |
| Rotorua Museum | (Blank) | Entertainment - Museums & Cultural |
| Politeknik Medan Phase-3 & 4 | (Blank) | Education - Higher Education |
| Eastpointe Commons Assisted Living | (Blank) | Healthcare - Senior Living |
| Ha Long Holiday Inn | (Blank) | Hospitality - Hotels & Resorts |
| Sydney Metro Protege X | (Blank) | Critical Infrastructure - Transportation |

---

## CSV Output: `opportunities_enhanced_verticals.csv`

The enhanced CSV contains:

| Column | Description |
|--------|-------------|
| Opportunity ID | Salesforce ID |
| Opportunity Name | Original name |
| Account Name | Integrator/partner |
| **Vertical** | **Original vertical** |
| **Enhanced_Vertical** | **NEW: Granular category** ⭐ |
| Industry | Industry field value |
| Stage | Opportunity stage |
| Amount (converted) | Deal value in NZD |
| Won | TRUE if won |
| Closed | TRUE if closed |
| Close Date | Date closed |
| Account Region | Geographic region |
| Closed Lost Reason | Why lost |

**Use this file to:**
1. ✅ Review suggested enhanced categories
2. ✅ Import enhanced verticals back into Salesforce
3. ✅ Create vertical-specific marketing campaigns
4. ✅ Segment email lists and content
5. ✅ Build reporting dashboards

---

## Recommendations for Further Improvement

### 1. Improve Opportunity Naming Convention (Critical)

**Current Problem:** 54.3% of opportunities still have generic categories because names lack keywords.

**Solution:** Implement naming standard for account managers:
```
Format: [End User Business Name] - [Business Type] - [Project Type]

Examples:
✅ "Hilton Downtown Seattle - Hotel - Access Control Upgrade"
✅ "Memorial Hospital - Healthcare - Campus Security System"
✅ "ABC Bank Branch 42 - Banking - Branch Security"
✅ "Riverside Apartments - Residential Multi-Family - New Build"

❌ "Project 123"
❌ "ABC Project"
❌ "Downtown Site"
```

**Expected Impact:** Could improve categorization from 54.3% to 85%+ with specific categories.

---

### 2. Make Enhanced_Vertical a Salesforce Field

**Action:** Add "Enhanced_Vertical" as a picklist field in Salesforce with these values:

**Commercial:**
- Commercial - Office Buildings
- Commercial - Mixed Use Development
- Commercial - Construction Projects
- Commercial - General

**Hospitality:**
- Hospitality - Hotels & Resorts
- Hospitality - Food & Beverage

**Healthcare:**
- Healthcare - Hospitals & Clinics
- Healthcare - Senior Living
- Healthcare - Dental
- Healthcare - General

**Education:**
- Education - Higher Education
- Education - K-12
- Education - Training Centers
- Education - General

**Government:**
- Government - General
- Government - Judicial
- Government - Libraries
- Government - Civic Buildings
- Government - Corrections

**Industrial:**
- Industrial - Manufacturing
- Industrial - Warehouse & Logistics
- Industrial - Heavy Industry

**Critical Infrastructure:**
- Critical Infrastructure - Aviation
- Critical Infrastructure - Ports & Maritime
- Critical Infrastructure - Transportation
- Critical Infrastructure - Utilities & Energy
- Critical Infrastructure - Data Centers
- Critical Infrastructure - General

**Entertainment:**
- Entertainment - Museums & Cultural
- Entertainment - Gaming & Casinos
- Entertainment - Sports Facilities
- Entertainment - Fitness & Recreation
- Entertainment - Theater & Arts

**Other:**
- Banking & Finance
- Retail
- Religious Facilities
- Residential - Multi-Family
- Residential - General
- Uncategorized

---

### 3. Immediate Campaign Priorities Based on Enhanced Data

#### Priority 1: Government Excellence Program ⭐
- **Category:** Government - General
- **Metrics:** 88 opps, 72.4% win rate, $8,501 avg deal
- **Action:** Create government procurement-focused campaign, GSA schedule promotion, public sector case studies

#### Priority 2: Banking & Finance Premium Positioning ⭐
- **Category:** Banking & Finance
- **Metrics:** 267 opps, 67.7% win rate, $10,389 avg deal
- **Action:** Financial services security campaign, compliance whitepapers, bank-specific solution packages

#### Priority 3: Multi-Family Housing Volume Play
- **Category:** Residential - Multi-Family
- **Metrics:** 1,024 opps, 38.7% win rate, $27,041 avg deal
- **Action:** Improve 38.7% win rate through property management partnerships, tenant security solutions

#### Priority 4: Aviation High-Value Focus 💰
- **Category:** Critical Infrastructure - Aviation
- **Metrics:** 32 opps, 48.3% win rate, **$52,242 avg deal**
- **Action:** Target airports and aviation facilities, critical infrastructure positioning, long sales cycle nurture

#### Priority 5: Hotel Market Investigation ⚠️
- **Category:** Hospitality - Hotels & Resorts
- **Metrics:** 43 opps, **17.9% win rate**, $13,501 avg deal
- **Action:** Investigate why win rate is so low, competitive analysis, identify solution gaps

---

## Next Steps

1. ✅ **Review CSV:** Examine `opportunities_enhanced_verticals.csv` and validate enhanced categories
2. ⬜ **Import to Salesforce:** Add Enhanced_Vertical field and import categorizations
3. ⬜ **Train Account Managers:** Implement new opportunity naming conventions
4. ⬜ **Launch Campaigns:** Start with Government and Banking & Finance segments
5. ⬜ **Monitor Performance:** Track win rates by enhanced vertical monthly
6. ⬜ **Iterate:** Refine categories based on campaign performance

---

## Conclusion

The enhanced categorization provides **40+ granular categories** instead of 17 broad ones, enabling much more targeted marketing campaigns. While only 2.5% additional opportunities could be categorized automatically (due to non-descriptive naming), the new structure provides:

✅ **Clearer segmentation** for high-performing verticals
✅ **Identification of problem areas** (Hotels, Entertainment)
✅ **High-value opportunities** (Aviation: $52K avg deal)
✅ **Volume opportunities** (Multi-Family: 1,024 opps)
✅ **Actionable campaign priorities**

**The biggest opportunity for improvement is implementing better opportunity naming conventions**, which could improve automatic categorization from 45.7% to 85%+.
