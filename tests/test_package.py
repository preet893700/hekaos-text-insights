"""Test script for hekaos-text-insights package."""

from hekaos_text_insights import analyze_text


def test_resume_text():
    """Test with resume-like text."""
    text = """
    Senior Python Developer with 5 years of experience in backend development.
    Built RESTful APIs using Django and Flask frameworks. Led a team of 3 engineers
    to deliver microservices architecture. Improved system performance by 40%.
    Bachelor's degree in Computer Science. Presented at tech conferences.
    """
    
    result = analyze_text(text)
    
    print("=" * 60)
    print("TEST 1: Resume Text")
    print("=" * 60)
    print(f"Keywords: {result['keywords']}")
    print(f"Insights: {result['insights']}")
    print(f"Readability Score: {result['readability_score']}")
    print()


def test_technical_text():
    """Test with technical documentation."""
    text = """
    This API endpoint accepts POST requests with JSON payload.
    The system uses Docker containers deployed on AWS Kubernetes cluster.
    Database queries are optimized using SQL indexing and caching strategies.
    React frontend communicates with Node.js backend via WebSocket connections.
    """
    
    result = analyze_text(text)
    
    print("=" * 60)
    print("TEST 2: Technical Documentation")
    print("=" * 60)
    print(f"Keywords: {result['keywords']}")
    print(f"Insights: {result['insights']}")
    print(f"Readability Score: {result['readability_score']}")
    print()


def test_simple_text():
    """Test with simple text."""
    text = "Hello world. This is a test. Python is great."
    
    result = analyze_text(text)
    
    print("=" * 60)
    print("TEST 3: Simple Text")
    print("=" * 60)
    print(f"Keywords: {result['keywords']}")
    print(f"Insights: {result['insights']}")
    print(f"Readability Score: {result['readability_score']}")
    print()


def test_empty_text():
    """Test with empty text."""
    result = analyze_text("")
    
    print("=" * 60)
    print("TEST 4: Empty Text")
    print("=" * 60)
    print(f"Keywords: {result['keywords']}")
    print(f"Insights: {result['insights']}")
    print(f"Readability Score: {result['readability_score']}")
    print()


def test_job_description():
    """Test with job description."""
    text = """
    We are seeking a talented Software Engineer to join our team.
    The ideal candidate will have experience with Python, JavaScript, and SQL.
    You will collaborate with stakeholders and manage project deliverables.
    Bachelor's degree required. Strong communication skills essential.
    """
    
    result = analyze_text(text)
    
    print("=" * 60)
    print("TEST 5: Job Description")
    print("=" * 60)
    print(f"Keywords: {result['keywords']}")
    print(f"Insights: {result['insights']}")
    print(f"Readability Score: {result['readability_score']}")
    print()


def test_error_handling():
    """Test error handling."""
    print("=" * 60)
    print("TEST 6: Error Handling")
    print("=" * 60)
    
    try:
        analyze_text(123)
        print("ERROR: Should have raised TypeError")
    except TypeError as e:
        print(f"✓ Correctly raised TypeError: {e}")
    
    try:
        analyze_text(None)
        print("ERROR: Should have raised TypeError")
    except TypeError as e:
        print(f"✓ Correctly raised TypeError: {e}")
    
    print()


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("HEKAOS-TEXT-INSIGHTS - PACKAGE TEST SUITE")
    print("=" * 60 + "\n")
    
    test_resume_text()
    test_technical_text()
    test_simple_text()
    test_empty_text()
    test_job_description()
    test_error_handling()
    
    print("=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()