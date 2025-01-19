import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ScrollArea } from '@/components/ui/scroll-area';
import MetricCard from './metric-card';
import PieChartCard from './pie-chart-card';
import ChallengesCard from './challenges-card';
import { DollarSign, TrendingUp, Users, Percent } from 'lucide-react';

export default function EconomyPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    economic_system,
    sectors,
    government_budget,
    credit_ratings,
    economic_metrics,
    top_economic_challenges,
  } = latestSnapshot.economy;

  return (
    <div className="space-y-4">
      {/* Top Metrics Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="GDP"
          valueKey="economy.economic_metrics.gross_domestic_product_gdp"
          icon={DollarSign}
        />
        <MetricCard
          snapshots={snapshots}
          title="GDP Growth"
          valueKey="economy.economic_metrics.gdp_annual_growth_rate"
          icon={TrendingUp}
        />
        <MetricCard
          snapshots={snapshots}
          title="Unemployment"
          valueKey="economy.economic_metrics.unemployment_rate"
          icon={Users}
        />
        <MetricCard
          snapshots={snapshots}
          title="Inflation"
          valueKey="economy.economic_metrics.inflation_rate"
          icon={Percent}
        />
      </div>

      {/* Economic System Overview and Challenges */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Economic System</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{economic_system}</p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Economic Challenges"
          challenges={top_economic_challenges}
        />
      </div>

      {/* Key Economic Indicators */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Currency & Exchange</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Currency</h4>
                <p className="text-sm text-muted-foreground">
                  {economic_metrics.currency?.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Credit Ratings</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Standard & Poor's</h4>
                <p className="text-sm text-muted-foreground">
                  {credit_ratings.standard__poors.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Moody's</h4>
                <p className="text-sm text-muted-foreground">
                  {credit_ratings.moodys.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Fitch</h4>
                <p className="text-sm text-muted-foreground">
                  {credit_ratings.fitch.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Social Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Labor Force Participation</h4>
                <p className="text-sm text-muted-foreground">
                  {economic_metrics.labor_force_participation_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Poverty Rate</h4>
                <p className="text-sm text-muted-foreground">
                  {economic_metrics.poverty_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Gini Coefficient</h4>
                <p className="text-sm text-muted-foreground">
                  {economic_metrics.gini_coefficient.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Average Annual Income</h4>
                <p className="text-sm text-muted-foreground">
                  {economic_metrics.average_annual_income.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Sector Distribution */}
      <div className="grid gap-4 md:grid-cols-2">
        <PieChartCard
          title="GDP by Sector"
          data={Object.values(sectors.sector_contributions_to_gdp)}
          snapshots={snapshots}
          valueKeyPrefix="economy.sectors.sector_contributions_to_gdp"
          span={1}
        />
        <PieChartCard
          title="Employment by Sector"
          data={Object.values(sectors.employment_by_sector)}
          snapshots={snapshots}
          valueKeyPrefix="economy.sectors.employment_by_sector"
          span={1}
        />
      </div>

      {/* Government Budget */}
      <div className="grid gap-4 md:grid-cols-2">
        <PieChartCard
          title="Government Revenue"
          data={Object.values(government_budget.government_revenue_composition)}
          snapshots={snapshots}
          valueKeyPrefix="economy.government_budget.government_revenue_composition"
          span={1}
        />
        <PieChartCard
          title="Government Expenditure"
          data={Object.values(
            government_budget.government_expenditure_composition
          )}
          snapshots={snapshots}
          valueKeyPrefix="economy.government_budget.government_expenditure_composition"
          span={1}
        />
      </div>

      {/* Sector Details */}
      <Card>
        <CardHeader>
          <CardTitle>Industry Sectors</CardTitle>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[400px]">
            <div className="space-y-4">
              {Object.entries(sectors.industries).map(([key, industry]) => (
                <div key={key} className="space-y-2">
                  <h4 className="font-semibold">{industry.key}</h4>
                  <p className="text-sm text-muted-foreground">
                    {industry.value}
                  </p>
                </div>
              ))}
            </div>
          </ScrollArea>
        </CardContent>
      </Card>
    </div>
  );
}
