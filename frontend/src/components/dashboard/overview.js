import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { BarChart } from '@/components/dashboard/bar-chart';
import { Table } from '@/components/dashboard/table';
import { Banknote, Users, Crown, Gauge } from 'lucide-react';

export default function OverviewPage({ snapshots, latest }) {
  return (
    <div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4 pb-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">GDP</CardTitle>
            <Banknote className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {latest?.economy.economic_metrics.gross_domestic_product_gdp.value.toLocaleString(
                'en-US',
                {
                  style: 'currency',
                  currency: 'USD',
                }
              )}
            </div>
            <p className="text-xs text-muted-foreground">
              +20.1% from last month
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Population</CardTitle>
            <Users className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {latest?.state_overview.basic_information.total_population.value.toLocaleString(
                'en-US'
              )}
            </div>
            <p className="text-xs text-muted-foreground">
              +180.1% from last month
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Approval Rating
            </CardTitle>
            <Crown className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {Math.round(
                latest?.government.government_metrics
                  .overall_head_of_stategovernment_approval_rating.value * 100
              )}
              %
            </div>
            <p className="text-xs text-muted-foreground">
              +19% from last month
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Human Development Index
            </CardTitle>
            <Gauge className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {latest?.people.people_metrics.human_development_index_hdi.value}
            </div>
            <p className="text-xs text-muted-foreground">
              +201 since last hour
            </p>
          </CardContent>
        </Card>
      </div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>GDP</CardTitle>
          </CardHeader>
          <CardContent className="pl-2">
            <BarChart
              data={snapshots.map((snap) => ({
                name: snap.date,
                total:
                  snap.economy.economic_metrics.gross_domestic_product_gdp
                    .value,
              }))}
            />
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Top Citizen Concerns</CardTitle>
          </CardHeader>
          <CardContent>
            <Table
              data={
                latest
                  ? Object.values(
                      latest.public_opinion.top_concerns_among_citizens
                    )
                  : []
              }
            />
          </CardContent>
        </Card>
      </div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>Approval Rating</CardTitle>
          </CardHeader>
          <CardContent className="pl-2">
            <BarChart
              data={snapshots.map((snap) => ({
                name: snap.date,
                total:
                  snap.government.government_metrics
                    .overall_head_of_stategovernment_approval_rating.value,
              }))}
            />
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Top Citizen Concerns</CardTitle>
          </CardHeader>
          <CardContent>
            <Table
              data={
                latest
                  ? Object.values(
                      latest.public_opinion.top_concerns_among_citizens
                    )
                  : []
              }
            />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
