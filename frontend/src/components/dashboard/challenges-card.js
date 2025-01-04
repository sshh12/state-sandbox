import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

export default function ChallengesCard({ title, challenges }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {Object.values(challenges).map((challenge) => (
            <div key={challenge.key}>
              <h4 className="font-medium mb-2">{challenge.key}</h4>
              <p className="text-sm text-muted-foreground">{challenge.value}</p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
