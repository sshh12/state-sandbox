import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import MetricCard from './metric-card';
import { GraduationCap, BookOpen, School, Building2 } from 'lucide-react';

export default function EducationPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const { education_system, literacy, education_metrics } =
    latestSnapshot.education;

  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          snapshots={snapshots}
          title="Adult Literacy Rate"
          valueKey="education.literacy.adult_literacy_rate"
          icon={BookOpen}
        />
        <MetricCard
          snapshots={snapshots}
          title="Years of Schooling"
          valueKey="education.education_metrics.average_years_of_schooling"
          icon={School}
        />
        <MetricCard
          snapshots={snapshots}
          title="University Enrollment"
          valueKey="education.education_metrics.university_enrollment_rate"
          icon={GraduationCap}
        />
        <MetricCard
          snapshots={snapshots}
          title="Gender Parity Index"
          valueKey="education.education_metrics.gender_parity_index_in_education"
          icon={Building2}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Education System Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{education_system}</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Literacy Demographics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Adult Literacy</h4>
                <p className="text-sm text-muted-foreground">
                  {literacy.adult_literacy_rate.raw} of adults are literate
                </p>
              </div>
              <div>
                <h4 className="font-medium mb-2">
                  Ethnic Literacy Distribution
                </h4>
                <p className="text-sm text-muted-foreground">
                  {literacy.ethnic_literacy.value}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Primary Education</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {education_metrics.primary_schools.raw}
            </div>
            <p className="text-sm text-muted-foreground mt-2">
              Primary Schools
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Secondary Education</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {education_metrics.secondary_schools.raw}
            </div>
            <p className="text-sm text-muted-foreground mt-2">
              Secondary Schools
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Higher Education</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {education_metrics.universities.raw}
            </div>
            <p className="text-sm text-muted-foreground mt-2">Universities</p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
