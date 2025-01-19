import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Palette, Building2, BookOpen, Music } from 'lucide-react';

export default function CulturePage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    cultural_identity,
    cultural_practices,
    cultural_metrics,
    top_cultural_challenges,
  } = latestSnapshot.culture;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Soft Power Index"
          valueKey="culture.cultural_metrics.soft_power_index"
          icon={Palette}
        />
        <MetricCard
          snapshots={snapshots}
          title="Cultural Centers"
          valueKey="culture.cultural_metrics.international_cultural_centers"
          icon={Building2}
        />
        <MetricCard
          snapshots={snapshots}
          title="Published Books"
          valueKey="culture.cultural_metrics.published_books_per_year"
          icon={BookOpen}
        />
        <MetricCard
          snapshots={snapshots}
          title="Concert Venues"
          valueKey="culture.cultural_metrics.concert_venues"
          icon={Music}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Cultural Identity</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {cultural_identity.map((item, index) => (
                <p key={index} className="text-sm text-muted-foreground">
                  • {item}
                </p>
              ))}
            </div>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Cultural Challenges"
          challenges={top_cultural_challenges}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Cultural Practices</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {cultural_practices.map((practice, index) => (
                <p key={index} className="text-sm text-muted-foreground">
                  • {practice}
                </p>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Cultural Facilities</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Protected Cultural Sites</h4>
                <p className="text-sm text-muted-foreground">
                  {cultural_metrics.protected_cultural_sites.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Art Galleries</h4>
                <p className="text-sm text-muted-foreground">
                  {cultural_metrics.art_galleries.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Museums</h4>
                <p className="text-sm text-muted-foreground">
                  {cultural_metrics.museums.raw}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Theaters</h4>
                <p className="text-sm text-muted-foreground">
                  {cultural_metrics.theaters.raw}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
