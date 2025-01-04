import { ReactSVG } from 'react-svg';

export function FlagSVG({ svgString }) {
  if (!svgString) return null;

  // Extract width and height from SVG string if they exist
  const widthMatch = svgString.match(/width="(\d+)"/);
  const heightMatch = svgString.match(/height="(\d+)"/);
  const width = widthMatch ? parseInt(widthMatch[1]) : 24;
  const height = heightMatch ? parseInt(heightMatch[1]) : 24;

  // Add or replace viewBox while preserving other attributes and formatting
  const modifiedSvgString = svgString.replace(/(<svg[^>]*)>/, (match, p1) => {
    // Remove existing viewBox if present
    const cleanedAttributes = p1.replace(/viewBox="[^"]*"/, '');
    return `${cleanedAttributes} viewBox="0 0 ${width} ${height}">`;
  });

  const svgBlob = new Blob([modifiedSvgString], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(svgBlob);

  return (
    <ReactSVG
      src={url}
      wrapper="span"
      onLoad={() => URL.revokeObjectURL(url)}
      beforeInjection={(svg) => {
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.style.height = '2rem';
        svg.style.width = 'auto';
        svg.style.display = 'inline-block';
        svg.style.verticalAlign = 'middle';
      }}
    />
  );
}
