import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import ReactMarkdown from 'react-markdown';
import { useState } from 'react';

export default function ExecutiveReport({ snapshots }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const report = snapshots[selectedIndex]?.delta_report;

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
        {snapshots.length > 0 && (
          <div className="px-6 py-4 border-t">
            <Select
              value={selectedIndex.toString()}
              onValueChange={(value) => setSelectedIndex(parseInt(value))}
            >
              <SelectTrigger className="w-[180px]">
                <SelectValue placeholder="Select year" />
              </SelectTrigger>
              <SelectContent>
                {snapshots.map((snapshot, index) => (
                  <SelectItem key={index} value={index.toString()}>
                    {snapshot.date}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
