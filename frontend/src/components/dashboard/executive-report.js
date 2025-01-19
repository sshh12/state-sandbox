import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import ReactMarkdown from 'react-markdown';

export default function ExecutiveReport({ snapshots }) {
  const report = snapshots[0]?.delta_report;
  return (
    <Card className="col-span-3">
      {!report && (
        <CardHeader>
          <CardTitle>Executive Report</CardTitle>
        </CardHeader>
      )}
      <CardContent className="p-0">
        <div className="max-h-[500px] overflow-y-auto px-6 py-4">
          {report ? (
            <div className="prose prose-sm dark:prose-invert max-w-none">
              <ReactMarkdown>{report}</ReactMarkdown>
            </div>
          ) : (
            <p className="text-sm text-muted-foreground">
              Play a turn to see changes in your nation.
            </p>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
