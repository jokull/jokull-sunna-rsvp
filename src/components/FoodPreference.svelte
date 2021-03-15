<script>
  export let value;
</script>

<label class="block">
  <span class="block pl-3">Matur</span>
  <select bind:value class="block w-full mt-0 border-0 bg-transparent select">
    <option value="vegan">Vegan</option>
    <option value="pescatarian">Fiskur</option>
    <option value="meat">Kjöt</option>
  </select>
</label>
