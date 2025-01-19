import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Table } from '@/components/dashboard/table';
import { Banknote, Users, Crown, Gauge } from 'lucide-react';
import MetricCard from './metric-card';
import EventsTimeline from './events-timeline';
import ExecutiveReport from './executive-report';

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
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Recent Headlines</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {snapshots[0]?.public_opinion.recent_headlines?.map(
                (headline, index) => (
                  <div
                    key={index}
                    className="p-4 rounded-lg border bg-card hover:bg-accent/50 transition-colors"
                  >
                    <p className="text-sm leading-relaxed">
                      {headline.replace(/^"|"$/g, '')}
                    </p>
                  </div>
                )
              )}
            </div>
            {!snapshots[0]?.public_opinion.recent_headlines && (
              <p className="text-sm text-muted-foreground">
                No recent headlines available.
              </p>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
