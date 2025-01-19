import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Mountain, TreePine, Wind, Droplets } from 'lucide-react';

export default function GeographyPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    geographic_features,
    natural_resource_production,
    environmental_metrics,
    top_environmental_challenges,
  } = latestSnapshot.geography_and_environment;

  if (!natural_resource_production || !environmental_metrics) return null;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Land Area"
          valueKey="geography_and_environment.environmental_metrics.total_land_area"
          icon={Mountain}
        />
        <MetricCard
          snapshots={snapshots}
          title="Air Quality Index"
          valueKey="geography_and_environment.environmental_metrics.air_quality_index"
          icon={Wind}
        />
        <MetricCard
          snapshots={snapshots}
          title="CO2 Emissions"
          valueKey="geography_and_environment.environmental_metrics.co_emissions"
          icon={TreePine}
        />
        <MetricCard
          snapshots={snapshots}
          title="PM2.5"
          valueKey="geography_and_environment.environmental_metrics.particulate_matter_pm"
          icon={Droplets}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Geographic Features</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              {geographic_features}
            </p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Environmental Challenges"
          challenges={top_environmental_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Natural Resource Production</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {natural_resource_production.oil_and_gas && (
                <div>
                  <h4 className="font-medium mb-2">Oil and Gas</h4>
                  <p className="text-sm text-muted-foreground">
                    {natural_resource_production.oil_and_gas.raw}
                  </p>
                </div>
              )}
              {natural_resource_production.coal && (
                <div>
                  <h4 className="font-medium mb-2">Coal</h4>
                  <p className="text-sm text-muted-foreground">
                    {natural_resource_production.coal.raw}
                  </p>
                </div>
              )}
              {natural_resource_production.precious_metals_goldsilver && (
                <div>
                  <h4 className="font-medium mb-2">Precious Metals</h4>
                  <p className="text-sm text-muted-foreground">
                    {natural_resource_production.precious_metals_goldsilver.raw}
                  </p>
                </div>
              )}
              {natural_resource_production.industrial_metals_copperiron && (
                <div>
                  <h4 className="font-medium mb-2">Industrial Metals</h4>
                  <p className="text-sm text-muted-foreground">
                    {
                      natural_resource_production.industrial_metals_copperiron
                        .raw
                    }
                  </p>
                </div>
              )}
              {natural_resource_production.strategic_metals_uraniumrare_earth && (
                <div>
                  <h4 className="font-medium mb-2">Strategic Metals</h4>
                  <p className="text-sm text-muted-foreground">
                    {
                      natural_resource_production
                        .strategic_metals_uraniumrare_earth.raw
                    }
                  </p>
                </div>
              )}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Environmental Statistics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {environmental_metrics.air_quality_index && (
                <div>
                  <h4 className="font-medium mb-2">Air Quality Index</h4>
                  <p className="text-sm text-muted-foreground">
                    {environmental_metrics.air_quality_index.raw}
                  </p>
                </div>
              )}
              {environmental_metrics.co_emissions && (
                <div>
                  <h4 className="font-medium mb-2">CO2 Emissions</h4>
                  <p className="text-sm text-muted-foreground">
                    {environmental_metrics.co_emissions.raw}
                  </p>
                </div>
              )}
              {environmental_metrics.particulate_matter_pm && (
                <div>
                  <h4 className="font-medium mb-2">
                    Particulate Matter (PM2.5)
                  </h4>
                  <p className="text-sm text-muted-foreground">
                    {environmental_metrics.particulate_matter_pm.raw}
                  </p>
                </div>
              )}
              {environmental_metrics.number_of_endangered_species && (
                <div>
                  <h4 className="font-medium mb-2">Endangered Species</h4>
                  <p className="text-sm text-muted-foreground">
                    {environmental_metrics.number_of_endangered_species.raw}
                  </p>
                </div>
              )}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
