import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Button } from '@/components/ui/button';
import { LineChart } from 'lucide-react';
import { useState } from 'react';
import { MetricLineChartDialog } from './metric-line-chart-dialog';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';
import {
  Prison,
  Shield,
  Gun,
  AlertTriangle,
  DollarSign,
  Pill,
  Globe,
  Binary,
  ShieldAlert,
  UserX,
  Gavel,
  Building,
  Briefcase,
} from 'lucide-react';

function CrimeMetricCard({ title, value, icon: Icon, snapshots, valueKey }) {
  const [showChart, setShowChart] = useState(false);

  return (
    <>
      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium">{title}</CardTitle>
          <div className="flex items-center gap-2">
            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 transition-colors hover:bg-primary hover:text-primary-foreground"
                    onClick={() => setShowChart(true)}
                  >
                    <LineChart className="h-4 w-4" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent>
                  <p>View trend over time</p>
                </TooltipContent>
              </Tooltip>
            </TooltipProvider>
            {Icon && <Icon className="h-4 w-4 text-muted-foreground" />}
          </div>
        </CardHeader>
        <CardContent>
          <p className="text-2xl font-bold">{value}</p>
        </CardContent>
      </Card>
      {snapshots && valueKey && (
        <MetricLineChartDialog
          isOpen={showChart}
          onOpenChange={setShowChart}
          title={title}
          snapshots={snapshots}
          valueKey={valueKey}
        />
      )}
    </>
  );
}

export default function CrimePage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const { justice_system, crime_metrics, black_market, top_crime_challenges } =
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
        <Card>
          <CardHeader>
            <CardTitle>Black Market</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{black_market}</p>
          </CardContent>
        </Card>
      </div>

      <ChallengesCard
        title="Top Crime Challenges"
        challenges={top_crime_challenges}
      />

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <CrimeMetricCard
          title="Violent Crimes"
          value={crime_metrics.violent_crimes.raw}
          icon={AlertTriangle}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.violent_crimes"
        />
        <CrimeMetricCard
          title="Property Crimes"
          value={crime_metrics.property_crimes.raw}
          icon={Building}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.property_crimes"
        />
        <CrimeMetricCard
          title="Financial Crimes"
          value={crime_metrics.financial_crimes.raw}
          icon={DollarSign}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.financial_crimes"
        />
        <CrimeMetricCard
          title="White-Collar Crimes"
          value={crime_metrics.whitecollar_crimes.raw}
          icon={Briefcase}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.whitecollar_crimes"
        />
        <CrimeMetricCard
          title="Drug-Related Crimes"
          value={crime_metrics.drugrelated_crimes.raw}
          icon={Pill}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.drugrelated_crimes"
        />
        <CrimeMetricCard
          title="Organized Crime"
          value={crime_metrics.organized_crime.raw}
          icon={Globe}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.organized_crime"
        />
        <CrimeMetricCard
          title="Cybercrime"
          value={crime_metrics.cybercrime.raw}
          icon={Binary}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.cybercrime"
        />
        <CrimeMetricCard
          title="Public Order Crimes"
          value={crime_metrics.public_order_crimes.raw}
          icon={ShieldAlert}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.public_order_crimes"
        />
        <CrimeMetricCard
          title="Sexual Crimes"
          value={crime_metrics.sexual_crimes.raw}
          icon={UserX}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.sexual_crimes"
        />
        <CrimeMetricCard
          title="State/Political Crimes"
          value={crime_metrics.statepolitical_crimes.raw}
          icon={Gavel}
          snapshots={snapshots}
          valueKey="crime.crime_metrics.statepolitical_crimes"
        />
      </div>
    </div>
  );
}
