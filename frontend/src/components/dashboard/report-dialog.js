'use client';

import ReactMarkdown from 'react-markdown';
import { Dialog, DialogContent } from '@/components/ui/dialog';

export function ReportDialog({ isOpen, onOpenChange, report }) {
  if (!report) return null;

  return (
    <Dialog open={isOpen} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-4xl max-h-[80vh] overflow-y-auto">
        <div className="prose prose-sm dark:prose-invert">
          <ReactMarkdown>{report}</ReactMarkdown>
        </div>
      </DialogContent>
    </Dialog>
  );
}
