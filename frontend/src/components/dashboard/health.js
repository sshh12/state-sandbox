import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import PieChartCard from './pie-chart-card';
import { Heart, Baby, UserPlus, Building2 } from 'lucide-react';

export default function HealthPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    health_system,
    life_expectancy,
    health_statistics,
    health_metrics,
    top_health_challenges,
  } = latestSnapshot.health;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Life Expectancy"
          valueKey="health.life_expectancy.average_life_expectancy_at_birth"
          icon={Heart}
        />
        <MetricCard
          snapshots={snapshots}
          title="Infant Mortality"
          valueKey="health.health_metrics.infant_mortality_rate"
          icon={Baby}
        />
        <MetricCard
          snapshots={snapshots}
          title="Physician Density"
          valueKey="health.health_metrics.physician_density"
          icon={UserPlus}
        />
        <MetricCard
          snapshots={snapshots}
          title="Hospital Beds"
          valueKey="health.health_metrics.hospital_bed_density"
          icon={Building2}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Healthcare System</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{health_system}</p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Health Challenges"
          challenges={top_health_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Life Expectancy Demographics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <h4 className="font-medium mb-2">Male</h4>
                  <p className="text-2xl font-bold">
                    {life_expectancy.male_life_expectancy.raw}
                  </p>
                </div>
                <div>
                  <h4 className="font-medium mb-2">Female</h4>
                  <p className="text-2xl font-bold">
                    {life_expectancy.female_life_expectancy.raw}
                  </p>
                </div>
              </div>
              <div>
                <h4 className="font-medium mb-2">Ethnic Distribution</h4>
                <p className="text-sm text-muted-foreground">
                  {life_expectancy.ethnic_life_expectancy.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Key Health Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Fertility Rate</h4>
                <p className="text-sm text-muted-foreground">
                  {health_metrics.total_fertility_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Maternal Mortality</h4>
                <p className="text-sm text-muted-foreground">
                  {health_metrics.maternal_mortality_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Child Mortality</h4>
                <p className="text-sm text-muted-foreground">
                  {health_metrics.child_mortality_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Gross Reproduction Rate</h4>
                <p className="text-sm text-muted-foreground">
                  {health_metrics.gross_reproduction_rate.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <PieChartCard
          title="Disease Statistics"
          data={Object.values(health_statistics.diseases)}
          snapshots={snapshots}
          valueKeyPrefix="health.health_statistics.diseases"
        />
        <PieChartCard
          title="Causes of Death"
          data={Object.values(health_statistics.causes_of_death_composition)}
          snapshots={snapshots}
          valueKeyPrefix="health.health_statistics.causes_of_death_composition"
        />
      </div>
    </div>
  );
}
