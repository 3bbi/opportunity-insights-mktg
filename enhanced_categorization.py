#!/usr/bin/env python3
"""
Enhanced Salesforce Opportunity Categorization
More aggressive keyword extraction and categorization for ALL opportunities
"""

import pandas as pd
import re
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

def load_data(filepath):
    """Load the CSV data"""
    print("Loading data...")
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(filepath, encoding='latin-1')
        except:
            df = pd.read_csv(filepath, encoding='ISO-8859-1')
    print(f"Loaded {len(df)} opportunities")
    return df

def extract_enhanced_category(row):
    """
    Enhanced categorization using Opportunity Name, Industry, and existing Vertical
    Returns a specific, granular category
    """
    opp_name = str(row['Opportunity Name']).lower() if pd.notna(row['Opportunity Name']) else ''
    industry = str(row['Industry']).lower() if pd.notna(row['Industry']) else ''
    current_vertical = str(row['Vertical']) if pd.notna(row['Vertical']) else ''

    # Combine for matching
    text = f"{opp_name} {industry}"

    # Priority-based categorization (most specific first)

    # HOSPITALITY
    if any(term in text for term in ['hotel', 'motel', 'inn ', 'resort', 'marriott', 'hilton',
                                      'hyatt', 'radisson', 'ramada', 'holiday inn', 'best western',
                                      'sheraton', 'westin', 'ritz', 'four seasons', 'intercontinental']):
        return 'Hospitality - Hotels & Resorts'

    if any(term in text for term in ['restaurant', 'cafe', 'coffee', 'brewery', 'bar ', 'pub ',
                                      'grill', 'bistro', 'diner', 'eatery', 'food service']):
        return 'Hospitality - Food & Beverage'

    # HEALTHCARE
    if any(term in text for term in ['hospital', 'medical center', 'health center', 'clinic',
                                      'emergency room', 'surgical', 'patient']):
        return 'Healthcare - Hospitals & Clinics'

    if any(term in text for term in ['assisted living', 'senior living', 'nursing home',
                                      'retirement home', 'aged care', 'care home', 'elder care',
                                      'senior care', 'retirement community']):
        return 'Healthcare - Senior Living'

    if any(term in text for term in ['dental', 'dentist', 'orthodont']):
        return 'Healthcare - Dental'

    if 'healthcare' in current_vertical.lower():
        return 'Healthcare - General'

    # EDUCATION
    if any(term in text for term in ['university', 'college', 'polytechnic', 'politeknik',
                                      'campus', 'grad school', 'undergraduate']):
        return 'Education - Higher Education'

    if any(term in text for term in ['school', 'classroom', 'academy', 'kindergarten',
                                      'preschool', 'elementary', 'primary school', 'secondary',
                                      'high school', 'middle school', 'k-12', 'k12']):
        return 'Education - K-12'

    if any(term in text for term in ['training center', 'training facility', 'learning center',
                                      'education center', 'vocational']):
        return 'Education - Training Centers'

    if 'education' in current_vertical.lower():
        return 'Education - General'

    # GOVERNMENT & PUBLIC
    if any(term in text for term in ['prison', 'jail', 'correctional', 'detention', 'penitentiary']):
        return 'Government - Corrections'

    if any(term in text for term in ['courthouse', 'court house', 'judicial', 'court building']):
        return 'Government - Judicial'

    if any(term in text for term in ['city hall', 'town hall', 'municipal building', 'civic center']):
        return 'Government - Civic Buildings'

    if any(term in text for term in ['library', 'libraries']):
        return 'Government - Libraries'

    if any(term in text for term in ['museum', 'gallery', 'cultural center', 'heritage']):
        return 'Entertainment - Museums & Cultural'

    if any(term in text for term in ['government', 'federal', 'state building', 'parliament',
                                      'council', 'ministry', 'department of', 'public works']):
        return 'Government - General'

    # FINANCIAL
    if any(term in text for term in ['bank', 'atm', 'credit union', 'financial institution',
                                      'branch bank', 'banking', 'citibank', 'wells fargo',
                                      'chase bank', 'bmo', 'td bank']):
        return 'Banking & Finance'

    # RESIDENTIAL
    if any(term in text for term in ['apartment', 'condo', 'condominium', 'residential tower',
                                      'residential building', 'suites', 'multi-family', 'multifamily',
                                      'apt', 'residential complex']):
        return 'Residential - Multi-Family'

    if any(term in text for term in ['residential', 'housing', 'townhouse', 'single family',
                                      'subdivision', 'housing development']) and 'multi' not in text:
        return 'Residential - General'

    if 'multi family' in current_vertical.lower() or 'multifamily' in current_vertical.lower():
        return 'Residential - Multi-Family'

    if 'residential' in current_vertical.lower():
        return 'Residential - General'

    # RETAIL & COMMERCIAL
    if any(term in text for term in ['retail', 'shop', 'store', 'mall', 'shopping center',
                                      'shopping centre', 'plaza', 'outlet', 'showroom']):
        return 'Retail'

    if any(term in text for term in ['warehouse', 'distribution center', 'distribution centre',
                                      'logistics', 'fulfillment', 'fulfilment', 'storage facility']):
        return 'Industrial - Warehouse & Logistics'

    if any(term in text for term in ['office building', 'office tower', 'office complex',
                                      'corporate', 'headquarters', 'office park', 'business park',
                                      'commercial office']):
        return 'Commercial - Office Buildings'

    if any(term in text for term in ['mixed use', 'mixed-use', 'commercial development',
                                      'commercial building', 'commercial complex']):
        return 'Commercial - Mixed Use Development'

    # ENTERTAINMENT & RECREATION
    if any(term in text for term in ['stadium', 'arena', 'sports complex', 'athletic center',
                                      'sports center', 'sports centre', 'velodrome', 'aquatic center']):
        return 'Entertainment - Sports Facilities'

    if any(term in text for term in ['gym', 'fitness', 'health club', 'recreation center',
                                      'recreation centre', 'rec center', 'community center']):
        return 'Entertainment - Fitness & Recreation'

    if any(term in text for term in ['casino', 'gaming', 'slots', 'poker room']):
        return 'Entertainment - Gaming & Casinos'

    if any(term in text for term in ['cinema', 'theater', 'theatre', 'performing arts',
                                      'concert hall', 'auditorium', 'film']):
        return 'Entertainment - Theater & Arts'

    if 'gaming' in current_vertical.lower():
        return 'Entertainment - Gaming & Casinos'

    # RELIGIOUS
    if any(term in text for term in ['church', 'chapel', 'cathedral', 'parish', 'diocese',
                                      'temple', 'mosque', 'synagogue', 'religious', 'monastery',
                                      'sanctuary', 'worship center']):
        return 'Religious Facilities'

    if 'religious' in current_vertical.lower():
        return 'Religious Facilities'

    # INDUSTRIAL & MANUFACTURING
    if any(term in text for term in ['factory', 'manufacturing', 'plant', 'production facility',
                                      'assembly', 'fabrication', 'processing plant']):
        return 'Industrial - Manufacturing'

    if any(term in text for term in ['industrial', 'biofarma', 'pharma', 'pharmaceutical',
                                      'chemical plant', 'refinery', 'mill']):
        return 'Industrial - Heavy Industry'

    if 'heavy industry' in current_vertical.lower():
        return 'Industrial - Heavy Industry'

    # CRITICAL INFRASTRUCTURE
    if any(term in text for term in ['airport', 'terminal', 'aviation', 'air cargo', 'airfield']):
        return 'Critical Infrastructure - Aviation'

    if any(term in text for term in ['port ', 'seaport', 'maritime', 'cargo terminal', 'shipping',
                                      'harbor', 'harbour', 'dock', 'wharf']):
        return 'Critical Infrastructure - Ports & Maritime'

    if any(term in text for term in ['railway', 'train station', 'metro', 'subway', 'transit',
                                      'bus depot', 'transportation hub']):
        return 'Critical Infrastructure - Transportation'

    if any(term in text for term in ['data center', 'datacenter', 'server farm', 'colocation']):
        return 'Critical Infrastructure - Data Centers'

    if any(term in text for term in ['water treatment', 'power plant', 'utility', 'substation',
                                      'energy', 'lng', 'oil ', 'gas ', 'petroleum', 'pipeline']):
        return 'Critical Infrastructure - Utilities & Energy'

    if 'aviation' in current_vertical.lower():
        return 'Critical Infrastructure - Aviation'

    if 'transportation' in current_vertical.lower():
        return 'Critical Infrastructure - Transportation'

    if 'critical infrastructure' in current_vertical.lower():
        return 'Critical Infrastructure - General'

    # SECURITY & PROFESSIONAL SERVICES (based on Industry field)
    if 'security installer' in industry or 'security' in industry:
        # This is our integrator, not the end-user vertical
        # Keep as Commercial unless we found something specific above
        pass

    # CONSTRUCTION & ENGINEERING (for construction projects)
    if any(term in text for term in ['construction site', 'building project', 'new build',
                                      'development project', 'construction project']):
        return 'Commercial - Construction Projects'

    # If current vertical is specific and not "Commercial", keep it
    if current_vertical and current_vertical not in ['Commercial', 'Other', 'nan', '']:
        # Map some existing verticals to our new structure
        if current_vertical == 'Training':
            return 'Education - Training Centers'
        elif current_vertical == 'Retail':
            return 'Retail'
        else:
            return current_vertical

    # Last resort: if it says "Commercial" but we haven't categorized it
    if current_vertical == 'Commercial':
        return 'Commercial - General'

    # If we still don't have a category
    return 'Uncategorized'

def analyze_categorization_changes(df):
    """Analyze the changes from original to new categorization"""
    print("\n" + "="*80)
    print("ENHANCED CATEGORIZATION ANALYSIS")
    print("="*80)

    # Add enhanced category
    df['Enhanced_Vertical'] = df.apply(extract_enhanced_category, axis=1)

    # Count original vs new
    original_blanks = df['Vertical'].isna().sum()
    original_commercial = (df['Vertical'] == 'Commercial').sum()

    new_uncategorized = (df['Enhanced_Vertical'] == 'Uncategorized').sum()
    new_commercial_general = (df['Enhanced_Vertical'] == 'Commercial - General').sum()

    print(f"\nOriginal State:")
    print(f"  Blank verticals: {original_blanks} ({original_blanks/len(df)*100:.1f}%)")
    print(f"  'Commercial' verticals: {original_commercial} ({original_commercial/len(df)*100:.1f}%)")
    print(f"  Total needing improvement: {original_blanks + original_commercial} ({(original_blanks + original_commercial)/len(df)*100:.1f}%)")

    print(f"\nEnhanced State:")
    print(f"  'Uncategorized': {new_uncategorized} ({new_uncategorized/len(df)*100:.1f}%)")
    print(f"  'Commercial - General': {new_commercial_general} ({new_commercial_general/len(df)*100:.1f}%)")
    print(f"  Total still general: {new_uncategorized + new_commercial_general} ({(new_uncategorized + new_commercial_general)/len(df)*100:.1f}%)")

    improvement = (original_blanks + original_commercial) - (new_uncategorized + new_commercial_general)
    print(f"\nImprovement: {improvement} opportunities now have specific categories ({improvement/len(df)*100:.1f}%)")

    # Show new category distribution
    print("\n--- Enhanced Vertical Distribution ---")
    category_counts = df['Enhanced_Vertical'].value_counts()

    for category, count in category_counts.items():
        pct = count/len(df)*100
        # Show win rate if we have closed opportunities
        closed_in_cat = df[(df['Enhanced_Vertical'] == category) & (df['Closed'] == True)]
        if len(closed_in_cat) > 0:
            win_rate = closed_in_cat['Won'].sum() / len(closed_in_cat) * 100
            print(f"  {category}: {count} ({pct:.1f}%) - Win Rate: {win_rate:.1f}%")
        else:
            print(f"  {category}: {count} ({pct:.1f}%)")

    # Show examples of re-categorizations
    print("\n--- Examples of Re-Categorizations ---")
    print("\nCommercial -> Specific Categories:")
    commercial_recategorized = df[(df['Vertical'] == 'Commercial') & (df['Enhanced_Vertical'] != 'Commercial - General')]

    if len(commercial_recategorized) > 0:
        examples = commercial_recategorized.groupby('Enhanced_Vertical').head(2)
        for _, row in examples.iterrows():
            print(f"  '{row['Opportunity Name'][:60]}' -> {row['Enhanced_Vertical']}")

    print("\nBlank -> Specific Categories:")
    blank_recategorized = df[df['Vertical'].isna() & (df['Enhanced_Vertical'] != 'Uncategorized')]

    if len(blank_recategorized) > 0:
        examples = blank_recategorized.groupby('Enhanced_Vertical').head(2)
        for _, row in examples.iterrows():
            print(f"  '{row['Opportunity Name'][:60]}' -> {row['Enhanced_Vertical']}")

    return df

def generate_enhanced_csv(df):
    """Generate enhanced CSV with new categories"""
    print("\n--- Generating Enhanced CSV ---")

    # Create output with all useful columns
    output_df = df[[
        'Opportunity ID',
        'Opportunity Name',
        'Account Name',
        'Vertical',  # Original
        'Enhanced_Vertical',  # New!
        'Industry',
        'Stage',
        'Amount (converted)',
        'Won',
        'Closed',
        'Close Date',
        'Account Region',
        'Closed Lost Reason'
    ]].copy()

    output_file = 'opportunities_enhanced_verticals.csv'
    output_df.to_csv(output_file, index=False)
    print(f"Enhanced data saved to: {output_file}")

    return output_file

def generate_category_performance_report(df):
    """Generate performance metrics by enhanced category"""
    print("\n" + "="*80)
    print("PERFORMANCE BY ENHANCED CATEGORY")
    print("="*80)

    # Calculate metrics by category
    categories = df['Enhanced_Vertical'].unique()
    metrics = []

    for category in categories:
        cat_df = df[df['Enhanced_Vertical'] == category]
        closed_df = cat_df[cat_df['Closed'] == True]
        won_df = cat_df[cat_df['Won'] == True]

        # Calculate value - need to parse the Amount
        total_value = 0
        for _, row in won_df.iterrows():
            if pd.notna(row['Amount (converted)']):
                try:
                    value_str = str(row['Amount (converted)'])
                    value_str = value_str.replace('NZD', '').replace('USD', '').replace('AUD', '').replace('CAD', '').replace(',', '').strip()
                    value = float(value_str) if value_str else 0
                    total_value += value
                except (ValueError, AttributeError):
                    pass

        avg_deal = total_value / len(won_df) if len(won_df) > 0 else 0
        win_rate = (len(won_df) / len(closed_df) * 100) if len(closed_df) > 0 else 0

        metrics.append({
            'category': category,
            'total_opps': len(cat_df),
            'closed': len(closed_df),
            'won': len(won_df),
            'win_rate': win_rate,
            'total_value': total_value,
            'avg_deal': avg_deal
        })

    # Sort by total opportunities
    metrics.sort(key=lambda x: x['total_opps'], reverse=True)

    print(f"\n{'Category':<50} {'Opps':<8} {'Closed':<8} {'Won':<8} {'Win%':<8} {'Avg Deal':<15}")
    print("-" * 110)

    for m in metrics:
        if m['total_opps'] >= 5:  # Only show categories with at least 5 opportunities
            print(f"{m['category']:<50} {m['total_opps']:<8} {m['closed']:<8} {m['won']:<8} "
                  f"{m['win_rate']:>6.1f}%  ${m['avg_deal']:>13,.0f}")

def main():
    """Main analysis function"""
    # Load data
    df = load_data('SF Opportunity Data.csv')

    # Run enhanced categorization
    df = analyze_categorization_changes(df)

    # Generate CSV
    generate_enhanced_csv(df)

    # Generate performance report
    generate_category_performance_report(df)

    print("\n" + "="*80)
    print("ENHANCED CATEGORIZATION COMPLETE")
    print("="*80)
    print("\nKey outputs:")
    print("1. opportunities_enhanced_verticals.csv - All opportunities with new Enhanced_Vertical column")
    print("\nThis categorization is more granular and actionable for marketing campaigns.")

if __name__ == "__main__":
    main()
