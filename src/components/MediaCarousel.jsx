
import { useState } from "react";
import "./MediaCarousel.css";

export default function MediaCarousel({ media = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const prevSlide = () => {
    setCurrentIndex((prev) => (prev === 0 ? media.length - 1 : prev - 1));
  };

  const nextSlide = () => {
    setCurrentIndex((prev) => (prev === media.length - 1 ? 0 : prev + 1));
  };

  if (!media.length) {
    return <p className="no-media">No media available for this recipe.</p>;
  }

  const currentMedia = media[currentIndex];

  return (
    <div className="carousel-container">
      <button onClick={prevSlide} className="nav-button left">
        ❮
      </button>

      <div className="carousel-slide">
        {currentMedia.type === "image" ? (
          <img src={currentMedia.url} alt={currentMedia.alt || "Recipe Media"} />
        ) : (
          <video controls>
            <source src={currentMedia.url} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        )}
        <p className="caption">{currentMedia.caption}</p>
      </div>

      <button onClick={nextSlide} className="nav-button right">
        ❯
      </button>

      <div className="carousel-dots">
        {media.map((_, i) => (
          <span
            key={i}
            className={`dot ${i === currentIndex ? "active" : ""}`}
            onClick={() => setCurrentIndex(i)}
          ></span>
        ))}
      </div>
    </div>
  );
}
