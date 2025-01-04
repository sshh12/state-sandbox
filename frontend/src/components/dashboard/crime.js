import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import LineChartCard from './line-chart-card';
import ChallengesCard from './challenges-card';
import {
  Prison,
  Shield,
  Gun,
  AlertTriangle,
  DollarSign,
  Pill,
  Globe,
  Binary,
  Scale,
  UserX,
  Gavel,
  Building,
  Briefcase,
  ShieldAlert,
} from 'lucide-react';

export default function CrimePage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const { justice_system, crime_metrics, top_crime_challenges } =
    latestSnapshot.crime;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Prison Population"
          valueKey="crime.crime_metrics.population_incarcerated"
          icon={Prison}
        />
        <MetricCard
          snapshots={snapshots}
          title="Violent Crime Rate"
          valueKey="crime.crime_metrics.violent_crimes"
          icon={AlertTriangle}
        />
        <MetricCard
          snapshots={snapshots}
          title="Gun Ownership"
          valueKey="crime.crime_metrics.gun_ownership_rate"
          icon={Gun}
        />
        <MetricCard
          snapshots={snapshots}
          title="Prison Capacity"
          valueKey="crime.crime_metrics.prison_capacity"
          icon={Shield}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Justice System Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{justice_system}</p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Crime Challenges"
          challenges={top_crime_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-3 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Violent Crimes
            </CardTitle>
            <AlertTriangle className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.violent_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Property Crimes
            </CardTitle>
            <Building className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.property_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Financial Crimes
            </CardTitle>
            <DollarSign className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.financial_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              White-Collar Crimes
            </CardTitle>
            <Briefcase className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.whitecollar_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Drug-Related Crimes
            </CardTitle>
            <Pill className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.drugrelated_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Organized Crime
            </CardTitle>
            <Globe className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.organized_crime.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Cybercrime</CardTitle>
            <Binary className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">{crime_metrics.cybercrime.raw}</p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Public Order Crimes
            </CardTitle>
            <ShieldAlert className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.public_order_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Sexual Crimes</CardTitle>
            <UserX className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.sexual_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              State/Political Crimes
            </CardTitle>
            <Gavel className="h-4 w-4 text-muted-foreground ml-2" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">
              {crime_metrics.statepolitical_crimes.raw}
            </p>
            <p className="text-sm text-muted-foreground">
              per 100,000 population
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
