import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import PieChartCard from './pie-chart-card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Zap, Signal, Wifi, Droplets, Building2, Road } from 'lucide-react';

export default function InfrastructurePage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    infrastructure,
    technologies,
    energy_source_composition,
    infrastructure_metrics,
    infrastructure_challenges,
  } = latestSnapshot.infrastructure_and_technology;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Total Electricity Generation"
          valueKey="infrastructure_and_technology.infrastructure_metrics.total_electricity_generation"
          icon={Zap}
        />
        <MetricCard
          snapshots={snapshots}
          title="Mobile Phone Coverage"
          valueKey="infrastructure_and_technology.infrastructure_metrics.mobile_phone_subscriptions"
          icon={Signal}
        />
        <MetricCard
          snapshots={snapshots}
          title="Internet Access"
          valueKey="infrastructure_and_technology.infrastructure_metrics.highspeed_internet_access"
          icon={Wifi}
        />
        <MetricCard
          snapshots={snapshots}
          title="Water Access"
          valueKey="infrastructure_and_technology.infrastructure_metrics.access_to_improved_water_sources"
          icon={Droplets}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Infrastructure Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{infrastructure}</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Technology Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{technologies}</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Transportation Infrastructure</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Roads</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.roads.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Railways</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.railways.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Airports</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.airports.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Ports and Harbors</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.ports_and_harbors.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Utility Access</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Electricity Access</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.access_to_electricity.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Improved Sanitation</h4>
                <p className="text-sm text-muted-foreground">
                  {infrastructure_metrics.access_to_improved_sanitation.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <ChallengesCard
          title="Infrastructure Challenges"
          challenges={infrastructure_challenges}
        />

        <PieChartCard
          title="Energy Source Distribution"
          data={Object.values(energy_source_composition)}
          snapshots={snapshots}
          valueKeyPrefix="infrastructure_and_technology.energy_source_composition"
        />
      </div>
    </div>
  );
}
