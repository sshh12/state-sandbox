import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import PieChartCard from './pie-chart-card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Globe2, ArrowUpRight, ArrowDownRight, DollarSign } from 'lucide-react';

export default function InternationalRelationsPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    diplomatic_relations,
    trade: {
      export_goods_composition,
      import_goods_composition,
      export_partner_composition,
      import_partner_composition,
      trade_metrics,
    },
    top_international_relations_challenges,
  } = latestSnapshot.international_relations;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Total Exports"
          valueKey="international_relations.trade.trade_metrics.total_exports"
          icon={ArrowUpRight}
        />
        <MetricCard
          snapshots={snapshots}
          title="Total Imports"
          valueKey="international_relations.trade.trade_metrics.total_imports"
          icon={ArrowDownRight}
        />
        <Card className="col-span-2">
          <CardHeader>
            <CardTitle>Diplomatic Relations</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              {diplomatic_relations}
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <ChallengesCard
          title="International Relations Challenges"
          challenges={top_international_relations_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-2">
        <PieChartCard
          title="Export Goods"
          data={Object.values(export_goods_composition)}
          snapshots={snapshots}
          valueKeyPrefix="international_relations.trade.export_goods_composition"
        />
        <PieChartCard
          title="Import Goods"
          data={Object.values(import_goods_composition)}
          snapshots={snapshots}
          valueKeyPrefix="international_relations.trade.import_goods_composition"
        />
        <PieChartCard
          title="Export Partners"
          data={Object.values(export_partner_composition)}
          snapshots={snapshots}
          valueKeyPrefix="international_relations.trade.export_partner_composition"
        />
        <PieChartCard
          title="Import Partners"
          data={Object.values(import_partner_composition)}
          snapshots={snapshots}
          valueKeyPrefix="international_relations.trade.import_partner_composition"
        />
      </div>
    </div>
  );
}
