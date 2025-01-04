import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Table } from '@/components/dashboard/table';
import { Banknote, Users, Crown, Gauge } from 'lucide-react';
import MetricCard from './metric-card';
import EventsTimeline from './events-timeline';
import ReactMarkdown from 'react-markdown';

export default function OverviewPage({ snapshots }) {
  return (
    <div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4 pb-4">
        <MetricCard
          snapshots={snapshots}
          title="Gross Domestic Product"
          valueKey="state_overview.basic_information.gross_domestic_product_gdp"
          icon={Banknote}
        />
        <MetricCard
          snapshots={snapshots}
          title="Population"
          valueKey="state_overview.basic_information.total_population"
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
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Latest Report</CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            <div className="max-h-[500px] overflow-y-auto px-6 py-4">
              {snapshots[0]?.delta_report ? (
                <div className="prose prose-sm dark:prose-invert max-w-none">
                  <ReactMarkdown>{snapshots[0].delta_report}</ReactMarkdown>
                </div>
              ) : (
                <p className="text-sm text-muted-foreground">
                  Play a turn to see changes in your nation.
                </p>
              )}
            </div>
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Top Citizen Concerns</CardTitle>
          </CardHeader>
          <CardContent>
            <Table
              data={
                snapshots[0]
                  ? Object.values(
                      snapshots[0].public_opinion.top_concerns_among_citizens
                    )
                  : []
              }
            />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
