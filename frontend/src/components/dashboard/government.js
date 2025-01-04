'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ScrollArea } from '@/components/ui/scroll-area';
import MetricCard from './metric-card';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Percent, AlertTriangle, ThumbsUp } from 'lucide-react';

export default function GovernmentPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  // Assuming the data is nested under a property in the snapshot
  const governmentData = latestSnapshot.government || {};
  const {
    government_system = {},
    policies = {},
    top_government_challenges = {},
  } = governmentData;

  // Format policies for display
  const policyCategories = Object.entries(policies || {}).map(
    ([category, policies]) => ({
      name: category
        .split('_')
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' '),
      policies: Object.values(policies),
    })
  );

  const governmentSystemValue = '' + government_system;

  return (
    <div className="space-y-4">
      {/* Top Metrics Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <MetricCard
          snapshots={snapshots}
          title="Corruption Perception Index"
          valueKey="government.government_metrics.corruption_perception_index_cpi"
          icon={AlertTriangle}
        />

        <MetricCard
          snapshots={snapshots}
          title="Public Opinion"
          valueKey="government.government_metrics.direction_of_country"
          icon={Percent}
        />

        <MetricCard
          snapshots={snapshots}
          title="Approval Rating"
          valueKey="government.government_metrics.overall_head_of_stategovernment_approval_rating"
          icon={ThumbsUp}
        />
      </div>

      {/* Government System and Challenges */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Government System</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              {governmentSystemValue}
            </p>
          </CardContent>
        </Card>

        {Object.keys(top_government_challenges).length > 0 && (
          <Card>
            <CardHeader>
              <CardTitle>Top Government Challenges</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {Object.entries(top_government_challenges).map(
                  ([key, challenge]) => (
                    <div key={key} className="space-y-2">
                      <h4 className="font-semibold">{challenge.key}</h4>
                      <p className="text-sm text-muted-foreground">
                        {challenge.value}
                      </p>
                    </div>
                  )
                )}
              </div>
            </CardContent>
          </Card>
        )}
      </div>

      {/* Policy Categories */}
      {policyCategories.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Government Policies</CardTitle>
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[400px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Category</TableHead>
                    <TableHead>Policies</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {policyCategories.map((category) => (
                    <TableRow key={category.name}>
                      <TableCell className="font-medium">
                        {category.name}
                      </TableCell>
                      <TableCell>
                        <div className="space-y-2">
                          {category.policies.map((policy) => (
                            <div key={policy.key} className="space-y-1">
                              <div className="font-medium text-sm">
                                {policy.key}
                              </div>
                              <div className="text-sm text-muted-foreground">
                                {policy.value}
                              </div>
                            </div>
                          ))}
                        </div>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
