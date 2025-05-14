// See DashboardView.vue for usage example
export const useSampleHook = () => {
  const useSample = async () => {
    const response = await fetch("http://localhost:8000/sample/test", {
      method: "POST",
      body: JSON.stringify({ name: "John", value: 10 }),
    });
    const data = await response.json();
    return data;
  };

  return {
    useSample,
  };
};

