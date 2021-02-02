<script>
  export let label;
  export let error = null;
  export let autocapitalize = "on";
  export let value = undefined;
</script>

<label class="block">
  <span class="">{label}</span>
  <input
    type="text"
    {autocapitalize}
    class={`mt-0 block w-full px-0.5 border-0 border-b border-black border-opacity-50 bg-transparent focus:ring-0 focus:border-black ${
      error ? "bg-yellow-200" : ""
    }`}
    placeholder=""
    bind:value
  />
</label>
