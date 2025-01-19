import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { format } from 'date-fns';
function parseEvent(eventString) {
  // Remove leading "- " if present
  const cleanedString = eventString.replace(/^- /, '');
  const match = cleanedString.match(/([^:]+): (.+)$/);
  if (!match) return { category: 'Other', content: cleanedString };
  return {
    category: match[1],
    content: match[2].trim(),
  };
}

function shouldShowEvent(event) {
  const { content } = parseEvent(event);
  return content !== 'None' && !content.includes('No notable');
}

export default function EventsTimeline({ snapshots }) {
  if (!snapshots?.length) return null;

  // Get all events from all snapshots with their dates
  const allEvents = snapshots
    .slice(1)
    .filter((snapshot) => snapshot.events?.length > 0)
    .map((snapshot) => ({
      date: snapshot.date,
      // Filter out "None" and "No notable events" entries
      events: snapshot.events.filter(shouldShowEvent),
    }))
    .filter((snapshot) => snapshot.events.length > 0); // Remove dates with no significant events

  if (allEvents.length === 0) {
    return (
      <Card className="col-span-3">
        <CardHeader>
          <CardTitle>Events Timeline</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            No notable events recorded
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="col-span-3 pb-2">
      <CardHeader>
        <CardTitle>Events Timeline</CardTitle>
      </CardHeader>
      <CardContent className="p-0">
        <div className="max-h-[500px] overflow-y-auto">
          <div className="space-y-1 px-6">
            {allEvents.map(({ date, events }, groupIndex) => (
              <div key={date} className="space-y-2">
                <div className="sticky top-0 bg-card z-10 py-1">
                  <h3 className="text-sm font-medium">
                    {format(new Date(date), 'yyyy')}
                  </h3>
                </div>
                <div className="space-y-4 relative">
                  <div
                    className="absolute top-0 bottom-0 left-[3.5px] w-[2px] bg-muted rounded"
                    style={{
                      display: events.length > 1 ? 'block' : 'none',
                    }}
                  />
                  {events.map((event, index) => {
                    const { category, content } = parseEvent(event);
                    return (
                      <div key={index} className="flex gap-4 relative">
                        <div className="w-2 h-2 rounded-full bg-background border-2 border-primary flex-shrink-0 z-10" />
                        <div className="flex-1 pt-1 pb-2">
                          <p className="text-xs font-medium text-muted-foreground mb-1">
                            {category}
                          </p>
                          <p className="text-sm text-foreground">{content}</p>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
