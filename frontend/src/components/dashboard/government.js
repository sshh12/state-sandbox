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
import { Percent, AlertTriangle, ThumbsUp, Crown, Scale } from 'lucide-react';

export default function GovernmentPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const {
    government_system,
    government_metadata,
    policies,
    political_participation,
    government_metrics,
    top_government_challenges,
  } = latestSnapshot.government;

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

  return (
    <div className="space-y-4">
      {/* Top Metrics Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Corruption Index"
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
        <MetricCard
          snapshots={snapshots}
          title="Democracy Index"
          valueKey="government.government_metrics.democracy_index"
          icon={Scale}
        />
      </div>

      {/* Government Metadata */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Government Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Type</h4>
                <p className="text-sm text-muted-foreground">
                  {government_metadata.government_type.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Head of State</h4>
                <p className="text-sm text-muted-foreground">
                  {government_metadata.head_of_stategovernment.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Official Name</h4>
                <p className="text-sm text-muted-foreground">
                  {government_metadata.country_official_name.value}
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">Capital City</h4>
                <p className="text-sm text-muted-foreground">
                  {government_metadata.capital_city.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>System Description</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{government_system}</p>
          </CardContent>
        </Card>
      </div>

      {/* Political Participation and Challenges */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Political Participation</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground whitespace-pre-line">
              {
                political_participation
                  .political_participation_in_glindavaria_is_predominantly_guided_by_religious_and_monarchical_structures_agerelated_participation
                  .value
              }
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
