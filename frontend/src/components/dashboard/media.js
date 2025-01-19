import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import PieChartCard from './pie-chart-card';
import MetricCard from './metric-card';
import { Newspaper, Clock, Share2, Signal, Users } from 'lucide-react';

export default function MediaPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    media_landscape,
    media_source_composition,
    news_coverage_composition,
    media_metrics,
  } = latestSnapshot.media;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Press Freedom Index"
          valueKey="media.media_metrics.press_freedom_index"
          icon={Newspaper}
        />
        <MetricCard
          snapshots={snapshots}
          title="Daily Media Consumption"
          valueKey="media.media_metrics.average_daily_media_consumption"
          icon={Clock}
        />
        <MetricCard
          snapshots={snapshots}
          title="Social Media Usage"
          valueKey="media.media_metrics.social_media_usage"
          icon={Share2}
        />
        <MetricCard
          snapshots={snapshots}
          title="Digital Infrastructure"
          valueKey="media.media_metrics.digital_divide_index_infrastructure"
          icon={Signal}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Media Landscape Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{media_landscape}</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Digital Divide</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Infrastructure</h4>
                <p className="text-sm text-muted-foreground">
                  {media_metrics.digital_divide_index_infrastructure.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Socioeconomic</h4>
                <p className="text-sm text-muted-foreground">
                  {media_metrics.digital_divide_index_socioeconomic.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <PieChartCard
          title="Media Source Distribution"
          data={Object.values(media_source_composition)}
          snapshots={snapshots}
          valueKeyPrefix="media.media_source_composition"
        />
        <PieChartCard
          title="News Coverage Distribution"
          data={Object.values(news_coverage_composition)}
          snapshots={snapshots}
          valueKeyPrefix="media.news_coverage_composition"
        />
      </div>
    </div>
  );
}
