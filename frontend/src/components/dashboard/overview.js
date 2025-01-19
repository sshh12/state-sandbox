import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Table } from '@/components/dashboard/table';
import { Banknote, Users, Crown, Gauge } from 'lucide-react';
import MetricCard from './metric-card';
import EventsTimeline from './events-timeline';
import ExecutiveReport from './executive-report';
import Headlines from './headlines';
import Quotes from './quotes';

export default function OverviewPage({ snapshots }) {
  return (
    <div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4 pb-4">
        <MetricCard
          snapshots={snapshots}
          title="Gross Domestic Product"
          valueKey="economy.economic_metrics.gross_domestic_product_gdp"
          icon={Banknote}
        />
        <MetricCard
          snapshots={snapshots}
          title="Population"
          valueKey="people.people_metrics.total_population"
          icon={Users}
        />
        <MetricCard
          snapshots={snapshots}
          title="Approval Rating"
          valueKey="government.government_metrics.overall_head_of_stategovernment_approval_rating"
          icon={Crown}
        />
        <MetricCard
          snapshots={snapshots}
          title="Human Development Index"
          valueKey="people.people_metrics.human_development_index_hdi"
          icon={Gauge}
        />
      </div>
      <div className="grid gap-4 md:grid-cols-6 lg:grid-cols-6 pb-4">
        <EventsTimeline snapshots={snapshots} />
        <ExecutiveReport snapshots={snapshots} />
        <Quotes snapshots={snapshots} />
        <Headlines snapshots={snapshots} />
      </div>
    </div>
  );
}
