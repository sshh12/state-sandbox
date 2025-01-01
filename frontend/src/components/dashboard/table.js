export function Table({ data }) {
  return (
    <div className="space-y-8">
      {data.map((item) => (
        <div className="flex items-center" key={item.key}>
          <div className="space-y-1">
            <p className="text-sm font-medium leading-none">{item.key}</p>
          </div>
          <div className="ml-auto font-medium">{item.raw}</div>
        </div>
      ))}
    </div>
  );
}
