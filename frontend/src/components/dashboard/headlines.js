import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { ExternalLink } from 'lucide-react';
import { useState } from 'react';
import HeadlineDialog from './headline-dialog';

export default function Headlines({ snapshots }) {
  const [selectedHeadline, setSelectedHeadline] = useState(null);

  return (
    <>
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
                  className="p-4 rounded-lg border bg-card hover:bg-accent/50 transition-colors cursor-pointer group"
                  onClick={() =>
                    setSelectedHeadline({
                      headline: headline.replace(/^"|"$/g, ''),
                      fullStory:
                        snapshots[0]?.public_opinion.full_stories?.[index],
                    })
                  }
                >
                  <div className="flex items-start gap-3">
                    <p className="text-sm leading-relaxed flex-1">
                      {headline.replace(/^"|"$/g, '')}
                    </p>
                    <ExternalLink className="h-4 w-4 flex-shrink-0 text-muted-foreground/50 group-hover:text-foreground transition-colors" />
                  </div>
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

      {selectedHeadline && (
        <HeadlineDialog
          isOpen={!!selectedHeadline}
          onClose={() => setSelectedHeadline(null)}
          headline={selectedHeadline.headline}
          fullStory={selectedHeadline.fullStory}
        />
      )}
    </>
  );
}
