import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { ExternalLink } from 'lucide-react';
import { useState } from 'react';
import CitizenDialog from './citizen-dialog';

function parseQuote(quoteStr) {
  const match = quoteStr.match(/^(.*?)\s*-\s*"(.*)"$/);
  if (!match) return { demographics: '', quote: quoteStr };

  const [_, demographics, quote] = match;
  const demoParts = demographics.match(/^(.*?)\s*\((.*?)\)$/);
  if (!demoParts) return { demographics, quote };

  const [__, name, details] = demoParts;
  const detailsList = details.split(', ');

  return {
    name,
    age: detailsList[0],
    gender: detailsList[1],
    race: detailsList[2],
    religion: detailsList[3],
    occupation: detailsList[4],
    income: detailsList[5],
    quote,
  };
}

export default function Quotes({ snapshots }) {
  const [selectedCitizen, setSelectedCitizen] = useState(null);

  return (
    <>
      <Card className="col-span-3">
        <CardHeader>
          <CardTitle>Recent Citizen Voices</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-6">
            {snapshots[0]?.public_opinion.recent_citizen_quotes?.map(
              (quoteStr, index) => {
                const parsedQuote = parseQuote(quoteStr);
                const {
                  name,
                  age,
                  gender,
                  race,
                  religion,
                  occupation,
                  income,
                  quote,
                } = parsedQuote;
                return (
                  <div
                    key={index}
                    className="p-4 rounded-lg border bg-card hover:bg-accent/50 transition-colors cursor-pointer group"
                    onClick={() =>
                      setSelectedCitizen({
                        ...parsedQuote,
                        biography:
                          snapshots[0]?.public_opinion.citizen_biographies?.[
                            index
                          ],
                      })
                    }
                  >
                    <div className="flex flex-col space-y-2">
                      <div className="flex items-start gap-2">
                        <div className="flex-1">
                          <div className="flex items-center gap-2 flex-wrap">
                            <span className="font-medium">{name}</span>
                            <div className="flex gap-1.5 flex-wrap">
                              <Badge variant="outline">{age}</Badge>
                              <Badge variant="outline">{gender}</Badge>
                              <Badge variant="outline">{race}</Badge>
                              <Badge variant="outline">{religion}</Badge>
                            </div>
                          </div>
                          <div className="flex gap-2 text-xs text-muted-foreground mt-2">
                            <span>{occupation}</span>
                            <span>•</span>
                            <span>{income}</span>
                          </div>
                        </div>
                        <ExternalLink className="h-4 w-4 flex-shrink-0 text-muted-foreground/50 group-hover:text-foreground transition-colors mt-1" />
                      </div>
                      <p className="text-sm leading-relaxed mt-2 italic">
                        "{quote}"
                      </p>
                    </div>
                  </div>
                );
              }
            )}
          </div>
          {!snapshots[0]?.public_opinion.recent_citizen_quotes && (
            <p className="text-sm text-muted-foreground">
              No recent quotes available.
            </p>
          )}
        </CardContent>
      </Card>

      {selectedCitizen && (
        <CitizenDialog
          isOpen={!!selectedCitizen}
          onClose={() => setSelectedCitizen(null)}
          citizen={selectedCitizen}
        />
      )}
    </>
  );
}
