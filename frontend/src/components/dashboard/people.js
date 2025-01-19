import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import PieChartCard from './pie-chart-card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Users, Heart, Brain, ArrowUpRight } from 'lucide-react';

export default function PeoplePage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    population_distribution: {
      gender_composition,
      sexuality_composition,
      urbanrural_composition,
      economic_composition,
      education_composition,
      ethnic_composition,
      language_composition,
      religious_composition,
      housing_composition,
      population_growth,
    },
    migration,
    people_metrics,
    top_people_challenges,
  } = latestSnapshot.people;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Total Population"
          valueKey="people.people_metrics.total_population"
          icon={Users}
        />
        <MetricCard
          snapshots={snapshots}
          title="World Happiness Score"
          valueKey="people.people_metrics.gallup_world_happiness_score"
          icon={Heart}
        />
        <MetricCard
          snapshots={snapshots}
          title="Human Development Index"
          valueKey="people.people_metrics.human_development_index_hdi"
          icon={Brain}
        />
        <MetricCard
          snapshots={snapshots}
          title="Social Mobility Index"
          valueKey="people.people_metrics.social_mobility_index"
          icon={ArrowUpRight}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Migration Trends</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{migration}</p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Challenges"
          challenges={top_people_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Population Growth</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Annual Growth Rate</h4>
                <p className="text-sm text-muted-foreground">
                  {population_growth.population_annual_growth_rate.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Ethnic Growth</h4>
                <p className="text-sm text-muted-foreground">
                  {population_growth.ethnic_population_growth.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Religious Growth</h4>
                <p className="text-sm text-muted-foreground">
                  {population_growth.religious_population_growth.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Economic Class Growth</h4>
                <p className="text-sm text-muted-foreground">
                  {population_growth.economic_class_population_growth.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Gender Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Gender Inequality Index</h4>
                <p className="text-sm text-muted-foreground">
                  {people_metrics.gender_inequality_index_gii.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">
                  Female Labor Force Participation
                </h4>
                <p className="text-sm text-muted-foreground">
                  {people_metrics.female_labor_force_participation_rate.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <PieChartCard
          title="Gender Distribution"
          data={Object.values(gender_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.gender_composition"
        />
        <PieChartCard
          title="Urban/Rural Distribution"
          data={Object.values(urbanrural_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.urbanrural_composition"
        />
        <PieChartCard
          title="Economic Class Distribution"
          data={Object.values(economic_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.economic_composition"
        />
        <PieChartCard
          title="Education Level Distribution"
          data={Object.values(education_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.education_composition"
        />
        <PieChartCard
          title="Ethnic Distribution"
          data={Object.values(ethnic_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.ethnic_composition"
        />
        <PieChartCard
          title="Religious Distribution"
          data={Object.values(religious_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.religious_composition"
        />
        <PieChartCard
          title="Language Distribution"
          data={Object.values(language_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.language_composition"
        />
        <PieChartCard
          title="Housing Distribution"
          data={Object.values(housing_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.housing_composition"
        />
        <PieChartCard
          title="Sexuality Distribution"
          data={Object.values(sexuality_composition)}
          snapshots={snapshots}
          valueKeyPrefix="people.population_distribution.sexuality_composition"
        />
      </div>
    </div>
  );
}
