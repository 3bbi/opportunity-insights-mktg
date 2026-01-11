#!/usr/bin/env python3
"""
Closed Lost Reasons Analysis
Comprehensive analysis of why opportunities are lost, with breakdowns by IDN status, vertical, and region
"""

import pandas as pd
from collections import Counter, defaultdict
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

def extract_closed_lost(df):
    """Extract only closed lost opportunities"""
    # Filter for Closed = True and Won = False
    closed_lost = df[(df['Closed'] == True) & (df['Won'] == False)].copy()
    print(f"\nTotal Closed Lost opportunities: {len(closed_lost)}")
    return closed_lost

def analyze_total_level(df):
    """Analyze closed lost reasons at total level"""
    print("\n" + "="*80)
    print("TOTAL LEVEL - CLOSED LOST REASONS ANALYSIS")
    print("="*80)

    # Overall statistics
    total_closed_lost = len(df)
    total_closed = df['Closed'].sum() if 'Closed' in df.columns else len(df)

    print(f"\nTotal Closed Lost: {total_closed_lost}")

    # Closed Lost Reason distribution
    print("\n--- Top Closed Lost Reasons ---")
    reason_counts = df['Closed Lost Reason'].value_counts(dropna=False)

    for reason, count in reason_counts.head(15).items():
        pct = count / total_closed_lost * 100
        if pd.isna(reason):
            print(f"  (Blank/No Reason): {count} ({pct:.1f}%)")
        else:
            print(f"  {reason}: {count} ({pct:.1f}%)")

    return reason_counts

def analyze_by_idn_status(df):
    """Analyze closed lost reasons by IDN status"""
    print("\n" + "="*80)
    print("CLOSED LOST ANALYSIS BY IDN STATUS")
    print("="*80)

    # IDN Status distribution
    idn_counts = df['IDN Status'].value_counts(dropna=False)
    total = len(df)

    print("\n--- Closed Lost by IDN Status ---")
    for status, count in idn_counts.items():
        pct = count / total * 100
        if pd.isna(status):
            print(f"  (Blank): {count} ({pct:.1f}%)")
        else:
            print(f"  {status}: {count} ({pct:.1f}%)")

    # Top reasons by IDN status
    print("\n--- Top Closed Lost Reasons by IDN Status ---")
    for status in ['Active', 'Not a Member', 'Pending']:
        status_df = df[df['IDN Status'] == status]
        if len(status_df) > 0:
            print(f"\n{status} ({len(status_df)} lost opps):")
            top_reasons = status_df['Closed Lost Reason'].value_counts().head(5)
            for reason, count in top_reasons.items():
                pct = count / len(status_df) * 100
                if pd.notna(reason):
                    print(f"  {reason}: {count} ({pct:.1f}%)")

    # Blank IDN Status
    blank_idn = df[df['IDN Status'].isna()]
    if len(blank_idn) > 0:
        print(f"\n(Blank IDN Status) ({len(blank_idn)} lost opps):")
        top_reasons = blank_idn['Closed Lost Reason'].value_counts().head(5)
        for reason, count in top_reasons.items():
            pct = count / len(blank_idn) * 100
            if pd.notna(reason):
                print(f"  {reason}: {count} ({pct:.1f}%)")

def analyze_by_vertical(df):
    """Analyze closed lost reasons by vertical"""
    print("\n" + "="*80)
    print("CLOSED LOST ANALYSIS BY VERTICAL")
    print("="*80)

    # Vertical distribution
    vertical_counts = df['Vertical'].value_counts(dropna=False)
    total = len(df)

    print("\n--- Closed Lost by Vertical ---")
    for vertical, count in vertical_counts.head(10).items():
        pct = count / total * 100
        if pd.isna(vertical):
            print(f"  (Blank): {count} ({pct:.1f}%)")
        else:
            print(f"  {vertical}: {count} ({pct:.1f}%)")

    # Top reasons by major verticals
    print("\n--- Top Closed Lost Reasons by Vertical ---")
    major_verticals = vertical_counts.head(8).index

    for vertical in major_verticals:
        if pd.isna(vertical):
            vertical_df = df[df['Vertical'].isna()]
            vertical_name = "(Blank)"
        else:
            vertical_df = df[df['Vertical'] == vertical]
            vertical_name = vertical

        if len(vertical_df) > 0:
            print(f"\n{vertical_name} ({len(vertical_df)} lost opps):")
            top_reasons = vertical_df['Closed Lost Reason'].value_counts().head(5)
            for reason, count in top_reasons.items():
                pct = count / len(vertical_df) * 100
                if pd.notna(reason):
                    print(f"  {reason}: {count} ({pct:.1f}%)")

def analyze_by_region(df):
    """Analyze closed lost reasons by region"""
    print("\n" + "="*80)
    print("CLOSED LOST ANALYSIS BY REGION")
    print("="*80)

    # Region distribution
    region_counts = df['Account Region'].value_counts(dropna=False)
    total = len(df)

    print("\n--- Closed Lost by Region ---")
    for region, count in region_counts.items():
        pct = count / total * 100
        if pd.isna(region):
            print(f"  (Blank): {count} ({pct:.1f}%)")
        else:
            print(f"  {region}: {count} ({pct:.1f}%)")

    # Detailed analysis by region
    print("\n" + "="*80)
    print("DETAILED REGIONAL ANALYSIS")
    print("="*80)

    for region in region_counts.index:
        if pd.isna(region):
            continue

        region_df = df[df['Account Region'] == region]
        print(f"\n{'='*80}")
        print(f"REGION: {region.upper()}")
        print(f"{'='*80}")
        print(f"Total Closed Lost: {len(region_df)}")

        # Top reasons
        print(f"\n--- Top Closed Lost Reasons in {region} ---")
        top_reasons = region_df['Closed Lost Reason'].value_counts().head(10)
        for reason, count in top_reasons.items():
            pct = count / len(region_df) * 100
            if pd.notna(reason):
                print(f"  {reason}: {count} ({pct:.1f}%)")

        # IDN Status breakdown
        print(f"\n--- IDN Status in {region} ---")
        idn_counts = region_df['IDN Status'].value_counts(dropna=False)
        for status, count in idn_counts.items():
            pct = count / len(region_df) * 100
            if pd.isna(status):
                print(f"  (Blank): {count} ({pct:.1f}%)")
            else:
                print(f"  {status}: {count} ({pct:.1f}%)")

        # Top verticals
        print(f"\n--- Top Verticals in {region} ---")
        vertical_counts = region_df['Vertical'].value_counts(dropna=False).head(5)
        for vertical, count in vertical_counts.items():
            pct = count / len(region_df) * 100
            if pd.isna(vertical):
                print(f"  (Blank): {count} ({pct:.1f}%)")
            else:
                print(f"  {vertical}: {count} ({pct:.1f}%)")

def analyze_idn_vertical_relationships(df):
    """Analyze relationships between IDN status and verticals"""
    print("\n" + "="*80)
    print("IDN STATUS & VERTICAL RELATIONSHIPS")
    print("="*80)

    # Cross-tabulation
    print("\n--- Closed Lost: IDN Status vs Vertical ---")

    # Get top verticals
    top_verticals = df['Vertical'].value_counts().head(5).index

    for vertical in top_verticals:
        if pd.notna(vertical):
            vert_df = df[df['Vertical'] == vertical]
            print(f"\n{vertical} ({len(vert_df)} lost opps):")

            idn_dist = vert_df['IDN Status'].value_counts(dropna=False)
            for status, count in idn_dist.items():
                pct = count / len(vert_df) * 100
                if pd.isna(status):
                    print(f"  (Blank): {count} ({pct:.1f}%)")
                else:
                    print(f"  {status}: {count} ({pct:.1f}%)")

                    # Top reason for this combination
                    combo_df = vert_df[vert_df['IDN Status'] == status]
                    if len(combo_df) > 0:
                        top_reason = combo_df['Closed Lost Reason'].value_counts().head(1)
                        if len(top_reason) > 0 and pd.notna(top_reason.index[0]):
                            print(f"    → Top reason: {top_reason.index[0]} ({top_reason.values[0]})")

def generate_insights_and_recommendations(df):
    """Generate actionable insights"""
    print("\n" + "="*80)
    print("KEY INSIGHTS & RECOMMENDATIONS")
    print("="*80)

    total = len(df)

    # Insight 1: Most common reasons
    print("\n1. MOST COMMON CLOSED LOST REASONS")
    top_5_reasons = df['Closed Lost Reason'].value_counts().head(5)
    top_5_total = top_5_reasons.sum()
    print(f"   Top 5 reasons account for {top_5_total} ({top_5_total/total*100:.1f}%) of all losses:")
    for reason, count in top_5_reasons.items():
        if pd.notna(reason):
            print(f"   - {reason}: {count}")

    # Insight 2: IDN Status impact
    print("\n2. IDN STATUS IMPACT")
    idn_groups = df.groupby('IDN Status').size().sort_values(ascending=False)
    for status, count in idn_groups.items():
        if pd.notna(status):
            pct = count / total * 100
            print(f"   - {status}: {count} losses ({pct:.1f}%)")

            # Most common reason for this IDN status
            status_df = df[df['IDN Status'] == status]
            top_reason = status_df['Closed Lost Reason'].value_counts().head(1)
            if len(top_reason) > 0 and pd.notna(top_reason.index[0]):
                reason_pct = top_reason.values[0] / len(status_df) * 100
                print(f"     Top reason: {top_reason.index[0]} ({reason_pct:.1f}%)")

    # Insight 3: Vertical vulnerability
    print("\n3. VERTICALS WITH HIGHEST LOSS RATES")
    vertical_groups = df.groupby('Vertical').size().sort_values(ascending=False).head(5)
    for vertical, count in vertical_groups.items():
        if pd.notna(vertical):
            print(f"   - {vertical}: {count} losses")
            vert_df = df[df['Vertical'] == vertical]
            top_reason = vert_df['Closed Lost Reason'].value_counts().head(1)
            if len(top_reason) > 0 and pd.notna(top_reason.index[0]):
                print(f"     Primary reason: {top_reason.index[0]}")

    # Insight 4: Regional patterns
    print("\n4. REGIONAL PATTERNS")
    region_groups = df.groupby('Account Region').size().sort_values(ascending=False)
    for region, count in region_groups.items():
        if pd.notna(region):
            pct = count / total * 100
            print(f"   - {region}: {count} losses ({pct:.1f}%)")

            region_df = df[df['Account Region'] == region]
            top_reason = region_df['Closed Lost Reason'].value_counts().head(1)
            if len(top_reason) > 0 and pd.notna(top_reason.index[0]):
                print(f"     Top reason: {top_reason.index[0]}")

    # Recommendations
    print("\n" + "="*80)
    print("STRATEGIC RECOMMENDATIONS")
    print("="*80)

    # Analyze pricing/competition issues
    pricing_related = df[df['Closed Lost Reason'].str.contains('ricing|heap|ost|ompetition', case=False, na=False)]
    if len(pricing_related) > 0:
        print(f"\n• PRICING/COMPETITION ({len(pricing_related)} losses, {len(pricing_related)/total*100:.1f}%)")
        print(f"  Action: Review pricing strategy, competitive positioning")

        # Which verticals/regions are most price sensitive?
        price_verticals = pricing_related['Vertical'].value_counts().head(3)
        print(f"  Most price-sensitive verticals:")
        for vert, count in price_verticals.items():
            if pd.notna(vert):
                print(f"    - {vert}: {count} losses")

    # Analyze decision/timing issues
    decision_related = df[df['Closed Lost Reason'].str.contains('ecision|elay|iming|ostpone', case=False, na=False)]
    if len(decision_related) > 0:
        print(f"\n• DECISION/TIMING ISSUES ({len(decision_related)} losses, {len(decision_related)/total*100:.1f}%)")
        print(f"  Action: Improve sales process, faster follow-up, better qualification")

    # Analyze budget issues
    budget_related = df[df['Closed Lost Reason'].str.contains('udget', case=False, na=False)]
    if len(budget_related) > 0:
        print(f"\n• BUDGET CONSTRAINTS ({len(budget_related)} losses, {len(budget_related)/total*100:.1f}%)")
        print(f"  Action: Better budget qualification, financing options, ROI positioning")

    # IDN recommendations
    not_member = df[df['IDN Status'] == 'Not a Member']
    if len(not_member) > 0:
        print(f"\n• IDN 'NOT A MEMBER' PARTNERS ({len(not_member)} losses, {len(not_member)/total*100:.1f}%)")
        print(f"  Action: Prioritize IDN recruitment, provide member incentives")
        top_not_member_reason = not_member['Closed Lost Reason'].value_counts().head(1)
        if len(top_not_member_reason) > 0:
            print(f"  Top loss reason for non-members: {top_not_member_reason.index[0]}")

def export_detailed_analysis(df):
    """Export detailed closed lost analysis to CSV"""
    print("\n--- Exporting Detailed Analysis ---")

    # Create summary by reason, IDN, and vertical
    summary_data = []

    for reason in df['Closed Lost Reason'].unique():
        if pd.notna(reason):
            reason_df = df[df['Closed Lost Reason'] == reason]

            summary_data.append({
                'Closed_Lost_Reason': reason,
                'Total_Count': len(reason_df),
                'Pct_of_Total': len(reason_df) / len(df) * 100,
                'Top_Vertical': reason_df['Vertical'].mode()[0] if len(reason_df['Vertical'].mode()) > 0 else 'N/A',
                'Top_Region': reason_df['Account Region'].mode()[0] if len(reason_df['Account Region'].mode()) > 0 else 'N/A',
                'Active_IDN': len(reason_df[reason_df['IDN Status'] == 'Active']),
                'Not_Member_IDN': len(reason_df[reason_df['IDN Status'] == 'Not a Member']),
                'Pending_IDN': len(reason_df[reason_df['IDN Status'] == 'Pending'])
            })

    summary_df = pd.DataFrame(summary_data)
    summary_df = summary_df.sort_values('Total_Count', ascending=False)

    output_file = 'closed_lost_reasons_summary.csv'
    summary_df.to_csv(output_file, index=False)
    print(f"Summary exported to: {output_file}")

    return summary_df

def main():
    """Main analysis function"""
    # Load data
    df = load_data('SF Opportunity Data.csv')

    # Extract closed lost opportunities
    closed_lost_df = extract_closed_lost(df)

    # Total level analysis
    analyze_total_level(closed_lost_df)

    # IDN Status analysis
    analyze_by_idn_status(closed_lost_df)

    # Vertical analysis
    analyze_by_vertical(closed_lost_df)

    # Regional analysis
    analyze_by_region(closed_lost_df)

    # Relationships
    analyze_idn_vertical_relationships(closed_lost_df)

    # Insights and recommendations
    generate_insights_and_recommendations(closed_lost_df)

    # Export summary
    export_detailed_analysis(closed_lost_df)

    print("\n" + "="*80)
    print("CLOSED LOST ANALYSIS COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
