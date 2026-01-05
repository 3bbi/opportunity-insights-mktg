#!/usr/bin/env python3
"""
Salesforce Opportunity Data Analysis
Analyzes opportunity data to extract marketing insights and improve vertical categorization
"""

import pandas as pd
import re
from collections import Counter, defaultdict
import warnings
warnings.filterwarnings('ignore')

def load_data(filepath):
    """Load the CSV data"""
    print("Loading data...")
    # Try different encodings
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(filepath, encoding='latin-1')
        except:
            df = pd.read_csv(filepath, encoding='ISO-8859-1')
    print(f"Loaded {len(df)} opportunities")
    return df

def analyze_verticals(df):
    """Analyze current vertical categorization"""
    print("\n" + "="*80)
    print("CURRENT VERTICAL ANALYSIS")
    print("="*80)

    # Count blanks
    blank_count = df['Vertical'].isna().sum()
    total = len(df)
    print(f"\nBlank Verticals: {blank_count} ({blank_count/total*100:.1f}%)")
    print(f"Populated Verticals: {total - blank_count} ({(total-blank_count)/total*100:.1f}%)")

    # Vertical distribution
    print("\n--- Vertical Distribution ---")
    vertical_counts = df['Vertical'].value_counts(dropna=False)
    for vertical, count in vertical_counts.items():
        if pd.isna(vertical):
            print(f"  (Blank): {count} ({count/total*100:.1f}%)")
        else:
            print(f"  {vertical}: {count} ({count/total*100:.1f}%)")

    # Analyze Commercial specifically
    commercial_df = df[df['Vertical'] == 'Commercial']
    print(f"\n--- Commercial Vertical Details ---")
    print(f"Total Commercial opportunities: {len(commercial_df)}")
    print(f"Percentage of all opportunities: {len(commercial_df)/total*100:.1f}%")

    return commercial_df

def extract_business_type_keywords(opp_name):
    """
    Extract potential business type keywords from opportunity names
    Returns a list of potential business type indicators
    """
    if pd.isna(opp_name):
        return []

    opp_name = str(opp_name).lower()
    keywords = []

    # Define business type patterns
    patterns = {
        # Hospitality
        'hotel': ['hotel', 'motel', 'inn ', 'resort', 'marriott', 'hilton', 'hyatt', 'radisson', 'ramada', 'holiday inn', 'best western'],
        'restaurant': ['restaurant', 'cafe', 'coffee', 'brewery', 'bar ', 'grill', 'bistro', 'diner', 'eatery'],

        # Healthcare
        'hospital': ['hospital', 'medical center', 'health center', 'clinic'],
        'senior_living': ['assisted living', 'senior living', 'nursing home', 'retirement home', 'aged care', 'care home'],
        'healthcare': ['health', 'medical', 'dental'],

        # Education
        'university': ['university', 'college', 'polytechnic', 'politeknik'],
        'school': ['school', 'classroom', 'academy', 'kindergarten', 'preschool'],
        'education': ['education', 'learning center', 'training center'],

        # Government & Public
        'government': ['government', 'council', 'city hall', 'courthouse', 'municipal'],
        'prison': ['prison', 'jail', 'correctional', 'detention'],
        'library': ['library'],
        'museum': ['museum'],

        # Financial
        'bank': ['bank', ' atm', 'credit union', 'financial'],

        # Residential
        'apartment': ['apartment', 'condo', 'condominium', 'residential building', 'residential tower', 'suites'],
        'residential': ['residential', 'housing', 'townhouse'],

        # Retail
        'retail': ['retail', 'shop', 'store', 'mall', 'shopping center', 'plaza'],
        'warehouse': ['warehouse', 'distribution center', 'logistics'],

        # Office & Commercial Real Estate
        'office': ['office building', 'office tower', 'office complex', 'corporate'],
        'commercial_building': ['commercial development', 'mixed use'],

        # Entertainment & Recreation
        'entertainment': ['cinema', 'theater', 'theatre', 'film', 'entertainment'],
        'sports': ['stadium', 'arena', 'gym', 'fitness', 'sports center'],
        'casino': ['casino', 'gaming'],

        # Religious
        'church': ['church', 'chapel', 'cathedral', 'parish', 'diocese'],
        'religious': ['temple', 'mosque', 'synagogue', 'religious'],

        # Industrial & Manufacturing
        'manufacturing': ['manufacturing', 'factory', 'plant', 'production'],
        'industrial': ['industrial', 'biofarma', 'pharma'],

        # Infrastructure
        'airport': ['airport', 'terminal'],
        'port': ['port ', 'maritime', 'cargo'],
        'utilities': ['water treatment', 'power plant', 'utility'],
        'data_center': ['data center', 'datacenter'],

        # Specialized
        'construction': ['construction site', 'building project', 'development project'],
    }

    for category, terms in patterns.items():
        for term in terms:
            if term in opp_name:
                keywords.append(category)
                break  # Only add once per category

    return keywords

def categorize_opportunities(df):
    """Analyze opportunity names and categorize them"""
    print("\n" + "="*80)
    print("OPPORTUNITY NAME ANALYSIS")
    print("="*80)

    # Extract keywords from all opportunities
    df['extracted_keywords'] = df['Opportunity Name'].apply(extract_business_type_keywords)
    df['has_keywords'] = df['extracted_keywords'].apply(lambda x: len(x) > 0)

    # Statistics
    print(f"\nOpportunities with identifiable business type in name: {df['has_keywords'].sum()} ({df['has_keywords'].sum()/len(df)*100:.1f}%)")

    # Count all extracted categories
    all_keywords = []
    for keywords in df['extracted_keywords']:
        all_keywords.extend(keywords)

    keyword_counts = Counter(all_keywords)
    print("\n--- Business Types Identified from Opportunity Names ---")
    for keyword, count in keyword_counts.most_common():
        print(f"  {keyword}: {count}")

    return keyword_counts

def analyze_commercial_opportunities(commercial_df):
    """Deep dive into Commercial vertical opportunities"""
    print("\n" + "="*80)
    print("COMMERCIAL VERTICAL - DETAILED ANALYSIS")
    print("="*80)

    # Extract keywords for commercial opportunities
    commercial_df['extracted_keywords'] = commercial_df['Opportunity Name'].apply(extract_business_type_keywords)
    commercial_df['has_keywords'] = commercial_df['extracted_keywords'].apply(lambda x: len(x) > 0)

    print(f"\nCommercial opportunities with identifiable business type: {commercial_df['has_keywords'].sum()} ({commercial_df['has_keywords'].sum()/len(commercial_df)*100:.1f}%)")

    # Count categories within Commercial
    all_keywords = []
    for keywords in commercial_df['extracted_keywords']:
        all_keywords.extend(keywords)

    commercial_keyword_counts = Counter(all_keywords)

    print("\n--- Sub-Categories within 'Commercial' Vertical ---")
    for keyword, count in commercial_keyword_counts.most_common():
        print(f"  {keyword}: {count}")

    # Show sample opportunities for top categories
    print("\n--- Sample Opportunities by Sub-Category ---")
    top_categories = [cat for cat, _ in commercial_keyword_counts.most_common(10)]

    for category in top_categories[:5]:  # Show top 5
        print(f"\n{category.upper()}:")
        samples = commercial_df[commercial_df['extracted_keywords'].apply(lambda x: category in x)]['Opportunity Name'].head(5)
        for i, sample in enumerate(samples, 1):
            print(f"  {i}. {sample}")

def analyze_blank_verticals(df):
    """Analyze opportunities with blank verticals"""
    print("\n" + "="*80)
    print("BLANK VERTICAL ANALYSIS")
    print("="*80)

    blank_df = df[df['Vertical'].isna()].copy()

    # Extract keywords
    blank_df['extracted_keywords'] = blank_df['Opportunity Name'].apply(extract_business_type_keywords)
    blank_df['has_keywords'] = blank_df['extracted_keywords'].apply(lambda x: len(x) > 0)

    print(f"\nBlank verticals that could be categorized: {blank_df['has_keywords'].sum()} ({blank_df['has_keywords'].sum()/len(blank_df)*100:.1f}%)")

    # Count categories
    all_keywords = []
    for keywords in blank_df['extracted_keywords']:
        all_keywords.extend(keywords)

    blank_keyword_counts = Counter(all_keywords)

    print("\n--- Potential Categories for Blank Verticals ---")
    for keyword, count in blank_keyword_counts.most_common(15):
        print(f"  {keyword}: {count}")

def analyze_win_loss_by_vertical(df):
    """Analyze win/loss rates by vertical"""
    print("\n" + "="*80)
    print("WIN/LOSS ANALYSIS BY VERTICAL")
    print("="*80)

    # Only look at closed opportunities
    closed_df = df[df['Closed'] == True].copy()

    print("\n--- Win Rate by Vertical ---")
    vertical_stats = closed_df.groupby('Vertical').agg({
        'Won': ['sum', 'count', 'mean']
    }).round(3)

    vertical_stats.columns = ['Wins', 'Total_Closed', 'Win_Rate']
    vertical_stats = vertical_stats.sort_values('Total_Closed', ascending=False)

    for vertical, row in vertical_stats.iterrows():
        vertical_name = vertical if not pd.isna(vertical) else "(Blank)"
        print(f"  {vertical_name}: {row['Wins']:.0f}/{row['Total_Closed']:.0f} = {row['Win_Rate']*100:.1f}%")

def generate_enhanced_categorization(df):
    """Generate a new categorization for all opportunities"""
    print("\n" + "="*80)
    print("ENHANCED CATEGORIZATION PROPOSAL")
    print("="*80)

    def suggest_vertical(row):
        """Suggest a vertical based on all available information"""
        # If vertical is already specific and not Commercial, keep it
        if not pd.isna(row['Vertical']) and row['Vertical'] not in ['Commercial', '']:
            return row['Vertical']

        # Extract keywords from opportunity name
        keywords = extract_business_type_keywords(row['Opportunity Name'])

        # Priority mapping - map extracted keywords to suggested verticals
        priority_map = {
            'hotel': 'Hospitality - Hotels',
            'restaurant': 'Hospitality - Food & Beverage',
            'hospital': 'Healthcare - Hospitals',
            'senior_living': 'Healthcare - Senior Living',
            'healthcare': 'Healthcare',
            'university': 'Education - Higher Education',
            'school': 'Education - K-12',
            'education': 'Education',
            'government': 'Government',
            'prison': 'Government - Corrections',
            'library': 'Government - Public Facilities',
            'museum': 'Entertainment - Cultural',
            'bank': 'Banking & Finance',
            'apartment': 'Residential - Multi-Family',
            'residential': 'Residential',
            'retail': 'Retail',
            'warehouse': 'Industrial - Logistics',
            'office': 'Commercial - Office',
            'commercial_building': 'Commercial - Mixed Use',
            'entertainment': 'Entertainment',
            'sports': 'Entertainment - Sports & Recreation',
            'casino': 'Entertainment - Gaming',
            'church': 'Religious',
            'religious': 'Religious',
            'manufacturing': 'Industrial - Manufacturing',
            'industrial': 'Industrial',
            'airport': 'Critical Infrastructure - Transportation',
            'port': 'Critical Infrastructure - Transportation',
            'utilities': 'Critical Infrastructure - Utilities',
            'data_center': 'Critical Infrastructure - Data Centers',
        }

        # Find the first matching category
        for keyword in keywords:
            if keyword in priority_map:
                return priority_map[keyword]

        # If no keywords found, return original or "Uncategorized"
        if not pd.isna(row['Vertical']):
            return row['Vertical']
        return 'Uncategorized'

    df['Suggested_Vertical'] = df.apply(suggest_vertical, axis=1)

    # Show the new distribution
    print("\n--- Proposed Vertical Distribution ---")
    suggested_counts = df['Suggested_Vertical'].value_counts()
    total = len(df)

    for vertical, count in suggested_counts.items():
        print(f"  {vertical}: {count} ({count/total*100:.1f}%)")

    # Compare changes
    print("\n--- Impact of Re-categorization ---")
    changes = df[df['Vertical'] != df['Suggested_Vertical']]
    print(f"Opportunities that would be re-categorized: {len(changes)} ({len(changes)/len(df)*100:.1f}%)")

    # Save enhanced data
    output_df = df[['Opportunity ID', 'Opportunity Name', 'Vertical', 'Suggested_Vertical',
                     'Stage', 'Amount (converted)', 'Won', 'Account Region']].copy()
    output_file = 'opportunities_with_suggested_verticals.csv'
    output_df.to_csv(output_file, index=False)
    print(f"\nEnhanced data saved to: {output_file}")

    return df

def generate_marketing_insights(df, keyword_counts):
    """Generate marketing insights and recommendations"""
    print("\n" + "="*80)
    print("MARKETING INSIGHTS & RECOMMENDATIONS")
    print("="*80)

    # Calculate total values by category
    df['extracted_keywords'] = df['Opportunity Name'].apply(extract_business_type_keywords)

    # Group by extracted categories and calculate metrics
    category_metrics = defaultdict(lambda: {'count': 0, 'won': 0, 'total_value': 0})

    for _, row in df.iterrows():
        # Handle Amount (converted) - clean and convert to float
        if pd.notna(row['Amount (converted)']):
            try:
                # Remove currency symbols and commas, convert to float
                value_str = str(row['Amount (converted)'])
                value_str = value_str.replace('NZD', '').replace('USD', '').replace('AUD', '').replace('CAD', '').replace(',', '').strip()
                value = float(value_str) if value_str else 0
            except (ValueError, AttributeError):
                value = 0
        else:
            value = 0

        for keyword in row['extracted_keywords']:
            category_metrics[keyword]['count'] += 1
            if row['Won'] == True:
                category_metrics[keyword]['won'] += 1
            if row['Closed'] == True and row['Won'] == True:
                category_metrics[keyword]['total_value'] += value

    # Convert to list and sort by count
    metrics_list = []
    for category, metrics in category_metrics.items():
        win_rate = (metrics['won'] / metrics['count'] * 100) if metrics['count'] > 0 else 0
        avg_deal_size = (metrics['total_value'] / metrics['won']) if metrics['won'] > 0 else 0

        metrics_list.append({
            'category': category,
            'opportunities': metrics['count'],
            'wins': metrics['won'],
            'win_rate': win_rate,
            'total_value': metrics['total_value'],
            'avg_deal_size': avg_deal_size
        })

    metrics_list.sort(key=lambda x: x['opportunities'], reverse=True)

    print("\n--- Market Segment Performance ---")
    print(f"{'Category':<25} {'Opps':<8} {'Wins':<8} {'Win Rate':<12} {'Total Value':<20} {'Avg Deal':<15}")
    print("-" * 100)

    for m in metrics_list[:20]:
        print(f"{m['category']:<25} {m['opportunities']:<8} {m['wins']:<8} {m['win_rate']:>10.1f}% "
              f"${m['total_value']:>18,.0f}  ${m['avg_deal_size']:>13,.0f}")

    print("\n--- Strategic Recommendations ---")

    # High volume segments
    high_volume = [m for m in metrics_list if m['opportunities'] >= 20][:5]
    print("\n1. HIGH VOLUME SEGMENTS (Focus for scale campaigns):")
    for m in high_volume:
        print(f"   - {m['category']}: {m['opportunities']} opportunities")

    # High win rate segments
    high_win_rate = [m for m in metrics_list if m['opportunities'] >= 10]
    high_win_rate.sort(key=lambda x: x['win_rate'], reverse=True)
    print("\n2. HIGH WIN RATE SEGMENTS (Focus for conversion optimization):")
    for m in high_win_rate[:5]:
        print(f"   - {m['category']}: {m['win_rate']:.1f}% win rate ({m['wins']}/{m['opportunities']})")

    # High value segments
    high_value = [m for m in metrics_list if m['wins'] >= 5]
    high_value.sort(key=lambda x: x['avg_deal_size'], reverse=True)
    print("\n3. HIGH VALUE SEGMENTS (Focus for enterprise campaigns):")
    for m in high_value[:5]:
        print(f"   - {m['category']}: ${m['avg_deal_size']:,.0f} average deal")

    # Emerging segments
    emerging = [m for m in metrics_list if 5 <= m['opportunities'] < 20]
    emerging.sort(key=lambda x: x['win_rate'], reverse=True)
    print("\n4. EMERGING SEGMENTS (Test and expand):")
    for m in emerging[:5]:
        print(f"   - {m['category']}: {m['opportunities']} opps, {m['win_rate']:.1f}% win rate")

def main():
    """Main analysis function"""
    # Load data
    df = load_data('SF Opportunity Data.csv')

    # Run analyses
    commercial_df = analyze_verticals(df)
    keyword_counts = categorize_opportunities(df)
    analyze_commercial_opportunities(commercial_df)
    analyze_blank_verticals(df)
    analyze_win_loss_by_vertical(df)
    df = generate_enhanced_categorization(df)
    generate_marketing_insights(df, keyword_counts)

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\nNext steps:")
    print("1. Review 'opportunities_with_suggested_verticals.csv' for enhanced categorization")
    print("2. Implement vertical standardization in Salesforce")
    print("3. Develop targeted campaigns for high-performing segments")
    print("4. Create training materials for account managers on proper categorization")

if __name__ == "__main__":
    main()
